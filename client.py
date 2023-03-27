import grpc
import threading
from datetime import datetime
import time

import tictactoe_pb2_grpc, tictactoe_pb2
from leader import GameCoordinator
from player import Player


def coordinator_moves(stub, node_id):
    response = stub.FetchSymbols(tictactoe_pb2.FetchSymbolsRequest())
    while not response.success:
        response = stub.FetchSymbols(tictactoe_pb2.FetchSymbolsRequest())

    print(f"Game is started! You are a COORDINATOR. PLayers' symbols: {response.players}")
    leader = GameCoordinator(leader_id=node_id, player_ids_symbols=response.players)

    # create a thread pool with 2 threads
    t1 = threading.Thread(target=leader.monitor_game, args=(stub,))
    t1.start()

    t2 = threading.Thread(target=leader.coordinator_console)
    t2.start()

    t3 = threading.Thread(target=leader.manage_timeout)
    t3.start()

    t1.join()


def player_moves(stub, node_id):
    response = stub.AssignSymbol(tictactoe_pb2.AssignSymbolRequest(node_id=node_id))
    print(f"Game is started! You are a PLAYER. Your symbol is: {response.symbol}")
    if response.symbol == 'X':
        print("You move first!")
    else:
        print("You move after another player.")
    # Do we need a Player class if all the commands will be executed by the leader?
    player = Player(node_id, response.symbol)
    while True:
        command_string = input("Enter a command to execute: ")
        if ' ' in command_string:
            command, args = command_string.split(' ')
            args = [args]
        else:
            command = command_string
            args = ['']
        response = stub.PlayerSendCommand(tictactoe_pb2.PlayerSendCommandRequest(
            node_id=node_id, command=command, args=args))
        message = response.message

        # Showing the table
        if command == 'List-board':
            print_board(message)
        else:
            print(message)

def print_board(data):
    if '-' not in data:
        print(data)
    else:
        rows = data.split('\n')[:3]  # Split rows by newline
        for row in rows:
            cells = row.split('\t')[:4] # Split cells by tab
            print(f"\n{cells[0]}\t{cells[1]}\t{cells[2]}")

def run():
    with grpc.insecure_channel('localhost:20048') as channel:
        stub = tictactoe_pb2_grpc.TicTacToeStub(channel)
        print("Joining the game...")
        response = stub.JoinGame(tictactoe_pb2.JoinGameRequest(timestamp=datetime.now().isoformat()))
        node_id = response.node_id
        print(f"You have joined the game. Id: {node_id}")

        response = stub.StartGame(tictactoe_pb2.StartGameRequest(node_id=node_id, timestamp=datetime.now().isoformat()))
        while not response.success:
            time.sleep(10)
            response = stub.StartGame(tictactoe_pb2.StartGameRequest(node_id=node_id, timestamp=datetime.now().isoformat()))

        if response.is_leader:
            coordinator_moves(stub, node_id)
        else:
            player_moves(stub, node_id)


if __name__ == '__main__':
    run()