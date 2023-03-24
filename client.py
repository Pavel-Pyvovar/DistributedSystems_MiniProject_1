import grpc
from datetime import datetime
from datetime import timedelta
import sys
import time
import threading

import tictactoe_pb2_grpc, tictactoe_pb2
from leader import GameCoordinator
from player import Player

def run():
    with grpc.insecure_channel('localhost:50051') as channel:

        stub = tictactoe_pb2_grpc.TicTacToeStub(channel)

        response = stub.JoinGame(tictactoe_pb2.JoinGameRequest(timestamp=datetime.now().isoformat()))

        print(response.node_id)

        # response = stub.StartGame(tictactoe_pb2.StartGameRequest(timestampt=datetime.now()))
        # request = None

        # node_id, is_leader, symbol = send_request_to_start_game(request)
        #
        # if is_leader:
        #     leader = GameCoordinator(node_id)
        # else:
        #     player = Player(node_id, symbol)

if __name__ == '__main__':
    run()