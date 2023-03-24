import grpc
from datetime import datetime
from datetime import timedelta
import sys
import time

import tictactoe_pb2_grpc, tictactoe_pb2
from leader import GameCoordinator
from player import Player

def run():
    with grpc.insecure_channel('localhost:20048') as channel:

        stub = tictactoe_pb2_grpc.TicTacToeStub(channel)

        response = stub.JoinGame(tictactoe_pb2.JoinGameRequest(timestamp=datetime.now().isoformat()))

        node_id = response.node_id

        response = stub.StartGame(tictactoe_pb2.StartGameRequest(node_id=node_id, timestamp=datetime.now().isoformat()))
        while not response.success:
            time.sleep(10)
            response = stub.StartGame(tictactoe_pb2.StartGameRequest(node_id=node_id, timestamp=datetime.now().isoformat()))
        print(response)


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