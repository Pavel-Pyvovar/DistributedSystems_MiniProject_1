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

    def JoinGame(self, request, context):
        initial_timestamp = request.timestamps

        if len(self.node_ids) == 0:
            self.node_ids.append(1)
        else:
            node_id = self.node_ids[-1]+1
            self.node_ids.append(node_id)

        return tictactoe_pb2.JoinGameResponse(node_id=node_id)


    def StartGame(self, request, context):
        """
        Set up the game environment.
         1. Synchronize nodes using their own internal clock with the Berkeley Algorithm.
         2. Elect a leader (game master)
        """
        if len(self.node_ids) == 0:
            self.node_ids.append(1)
        else:
            node_id = self.node_ids[-1]+1
            self.node_ids.append(node_id)

        # If we have not elected a leader yet
        # if len(self.node_ids >= 3):
        #     self.leader_id = elect_leader()
        #
        # syncronize_nodes(self.node_ids, self.leader_id)

        is_leader = True if self.leader_id == node_id else False

        symbol = ''
        if node_id != self.leader_id and self.symbols:
            symbol = self.symbols.pop()

        self.responses[node_id] = tictactoe_pb2.StartGameResponse(
            node_id=node_id, is_leader=is_leader, symbol=symbol)


        # Note that assigning symbols for more than two players requires a different approach
        return tictactoe_pb2.StartGameResponse(
            node_id=node_id, is_leader=is_leader, symbol=symbol)

    def SetSymbol(self, request, context):
        """
        This command is used by a player during its turn to fill
         the board with its assigned symbol.
        """
        pass

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
    # TODO: Agree upon node id format
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