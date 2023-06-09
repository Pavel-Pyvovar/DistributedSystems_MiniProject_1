from queue import Queue
import grpc
from concurrent import futures
import time
import tictactoe_pb2
import tictactoe_pb2_grpc
from leader_election import elect_leader
from node_syncronization import syncronize_nodes


class TicTacToeServicer(tictactoe_pb2_grpc.TicTacToeServicer):

    def __init__(self):
        self.node_ids = []
        self.leader_id = None
        # Will be taken care of by the Berkeley algorithm
        self.timestamps = []
        self.symbols = ['X', 'O']
        self.responses = {}
        self.players = {}
        self.is_busy = False
        self.coordinator_done = False
        self.coordinator_reply = []
        self.player_commands = [] # potentially should replace player_moves

    def JoinGame(self, request, context):
        initial_timestamp = request.timestamp

        node_id = 1 if len(self.node_ids) == 0 else self.node_ids[-1]+1

        self.node_ids.append(node_id)

        return tictactoe_pb2.JoinGameResponse(node_id=node_id)


    def StartGame(self, request, context):
        """
        Set up the game environment.
         1. Synchronize nodes using their own internal clock with the Berkeley Algorithm.
         2. Elect a leader (game master)
        """
        # initial assignments
        success = False
        is_leader = False

        if len(self.node_ids) >= 3:
            # Elect a leader
            self.leader_id = max(self.node_ids)
            is_leader = self.leader_id == request.node_id

            syncronize_nodes(self.node_ids, self.leader_id)
            success = True

        # Note that assigning symbols for more than two players requires a different approach
        return tictactoe_pb2.StartGameResponse(
            success=success, is_leader=is_leader)

    def AssignSymbol(self, request, context):
        symbol = self.symbols.pop()
        self.players[request.node_id] = symbol
        return tictactoe_pb2.AssignSymbolResponse(symbol=symbol)

    def FetchSymbols(self, request, context):
        success = False
        if not self.symbols:
            success = True
        return tictactoe_pb2.FetchSymbolsResponse(success=success, players=self.players)

    def PlayerSendCommand(self, request, context):
        print(f"New request from {request.node_id}")
        if not self.is_busy:
            print(f"New request from {request.node_id} accepted.")
            self.is_busy = True
            self.coordinator_done = False
            node_id, command, args = request.node_id, request.command, request.args
            self.player_commands.append((node_id, command, args))

            while not self.coordinator_done:
                time.sleep(5)

            print(f"Sending info {self.coordinator_reply} from the coord to the player {request.node_id}...")
            self.is_busy = False
            return tictactoe_pb2.PlayerSendCommandResponse(
                success=self.coordinator_reply[0], message=self.coordinator_reply[1])
        else:
            return tictactoe_pb2.PlayerSendCommandResponse(success=False, message="Server is busy. Try later.")

    def CoordinatorAcceptCommand(self, request, context):
        while not self.is_busy:
            time.sleep(5)
        while not self.player_commands:
            time.sleep(1)
        node_id, command, args = self.player_commands.pop()
        print(f"Server passed the command {command} with args {args} from node {node_id} to the coordinator")
        return tictactoe_pb2.CoordinatorAcceptCommandResponse(node_id=node_id, command=command, args=args)

    def CoordinatorSendCommandResult(self, request, context):
        print(f"Coordinator replied")
        self.coordinator_reply = []
        self.coordinator_reply.append(request.success)
        self.coordinator_reply.append(request.message)
        self.coordinator_done = True
        return tictactoe_pb2.CoordinatorSendCommandResultResponse(success=True)


    def ListBoard(self, request, context):
        """
        This command lists the current state of the board
        from any player or from the game master.
        """
        pass

    def SetNodeTime(self, request, context):
        """
        Modify the internal clock of a specific Node.
        Leader can modify any clock in the system,
         whereas players can only modify their internal clock
        """
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tictactoe_pb2_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(), server)
    server.add_insecure_port('[::]:20048')
    server.start()
    print("Server started listening on DESIGNATED port")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()