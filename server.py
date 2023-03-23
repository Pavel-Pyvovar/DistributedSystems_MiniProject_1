import grpc
from concurrent import futures
import time
# Import compiled grpc files
import tictactoe_pb2
import tictactoe_pb2_grpc


# Define a servicer class
class TicTacToeServicer(tictactoe_pb2_grpc.TicTacToeServicer):

    def __init__(self):
        self.node_ids = []
        self.leader_id = None
        # Will be taken care of by the Berkely algorithm
        self.timestamps = []

    def fetchCommand(self, request, context):
        pass

    def addSymbolsToBoard(self, request, context):
        pass

    def StartGame(self, request, context):

        if request.id == 3:
            pass

class PlayerServicer(tictactoe_pb2_grpc.TicTacToeServicer):
    pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Bind servicer to the server
    tictactoe_pb2_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(), server)
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