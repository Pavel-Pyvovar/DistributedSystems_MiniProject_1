import grpc
from concurrent import futures
import time
import tictactoe_pb2
import tictactoe_pb2_grpc
from DistributedSystems_MiniProject_1.leader_election import elect_leader
from DistributedSystems_MiniProject_1.node_syncronization import syncronize_nodes


class TicTacToeServicer(tictactoe_pb2_grpc.TicTacToeServicer):

    def __init__(self, leader_id):
        self.node_ids = []
        self.leader_id = leader_id
        # Will be taken care of by the Berkely algorithm
        self.timestamps = []
        self.leader_assigned = False

    def StartGame(self, request, context):
        """
        Set up the game environment.
         1. Synchronize nodes using their own internal clock with the Berkeley Algorithm.
         2. Elect a leader (game master)
        """
        node_ids = request.node_ids
        syncronize_nodes(node_ids)
        self.leader_id = elect_leader(node_ids)
        # Note that assigning symbols for more than two players requires a different approach
        symbols = {n_id: s for n_id, s in zip(node_ids, ["X", "O"])}
        return tictactoe_pb2.StartGameReplyResult(leader_id=self.leader_id, symbols=symbols)

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
    # Bind servicer to the server
    # TODO: Agree upon node id format
    node_ids = [1, 2, 3]
    tictactoe_pb2_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(node_ids), server)
    server.add_insecure_port('[::]:20048')
    server.start()
    print("Server started listening on DESIGNATED port")
    # Accept command request
    # Store symbols
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()