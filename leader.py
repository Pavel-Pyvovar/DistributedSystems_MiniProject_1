import time
from queue import Queue

import tictactoe_pb2


class GameCoordinator:
    """Leader that is responsible for managing the tictactoe game"""

    def __init__(self, leader_id, player_ids_symbols: dict, board_size=3):
        self.leader_id = leader_id  # check if we need it
        # I think should be initialized here, not from outside
        self.board_size = board_size
        self.board = [['-'] * self.board_size for _ in range(self.board_size)]  # 'empty' positions are marked as '-'
        self.player_ids_symbols = player_ids_symbols
        # a queue to store info about next move
        self.next_move_id = Queue()
        self.next_move_id.put(list(player_ids_symbols.keys())[list(player_ids_symbols.values()).index('X')])
        self.next_move_id.put(list(player_ids_symbols.keys())[list(player_ids_symbols.values()).index('O')])
        self.commands = {"Set-symbol": self.set_symbol, "List-board": self.list_board}
        self.winner_id = 0
        self.game_finished = False
        self.reset_time_counter = 0
        self.timeout_happened = False

    # return a symbol of a winner
    def check_winner(self) -> str:
        """Decide if there is a winner"""
        # This function probably should be called after every move
        # of any player to see if any row/column/diagonal is filled
        # with the same symbol
        results = []

        # check diagonals
        symbol = self.board[0][0]
        for i in range(1, self.board_size):
            if symbol != self.board[i][i]:
                symbol = '-'
                break
        results.append(symbol)

        symbol = self.board[self.board_size - 1][0]
        for i in range(1, self.board_size):
            if symbol != self.board[self.board_size - 1 - i][i]:
                symbol = '-'
                break
        results.append(symbol)

        # horisontal lines
        for i in range(self.board_size):
            symbol = self.board[i][0]
            for j in range(1, self.board_size):
                if symbol != self.board[i][j]:
                    symbol = '-'
                    break
            results.append(symbol)

        # vertical lines
        for i in range(self.board_size):
            symbol = self.board[0][i]
            for j in range(1, self.board_size):
                if symbol != self.board[j][i]:
                    symbol = '-'
                    break
            results.append(symbol)

        results = [x for x in results if x != '-']
        if len(results) > 0:
            return results[0]
        else:
            return '-'

    def monitor_game(self, stub):
        while True:
            response = stub.CoordinatorAcceptCommand(tictactoe_pb2.CoordinatorAcceptCommandRequest())
            self.reset_time_counter = 0
            
            print(f"Timer was reset to {self.reset_time_counter}")
            node_id, command, args = response.node_id, response.command, response.args

            method = self.commands.get(command)
            if method:
                if not self.timeout_happened:
                    success, message = method(node_id, *args)
                else:
                    self.timeout_happened = False
                    success = False
                    message = f"Timeout happened!"
            else:
                success = False
                message = f"Command {command} does not exist!"

            response = stub.CoordinatorSendCommandResult(
                tictactoe_pb2.CoordinatorSendCommandResultRequest(success=success, message=message))

            if response.success:
                print("Player is successfully notified about the result.")
            else:
                print("Player is not notified about the result.")

    def coordinator_console(self):
        while True:
            command = input("Input a command (if new text appears in the console, you still are able to run a command): \n")
            method = self.commands.get(command)

            if method:
                output = method(self.leader_id, None)
                if command == "List-board":
                    self.print_board(output[1])

    def set_symbol(self, node_id, position):
        # Node id when passed in args through GRPC has to be converted to a string
            
        position = [int(c) for c in position.split(',')]
        for number in position:
            if number > 2:
                return False, f"Invalid position {position}, enter again."

        symbol = self.player_ids_symbols[node_id]

        if self.next_move_id.queue[0] != node_id:
            return False, "Is it not your turn."

        if self.board[position[0]][position[1]] != '-':
            return False, "This position is already taken."

        self.board[position[0]][position[1]] = symbol
        print(f"Symbol {symbol} is added from player {node_id}.")

        # switching the queue
        self.next_move_id.put(self.next_move_id.get())

        if self.check_winner() == '-':
            # Setting winner_id to 0 because there are no winners
            self.winner_id = 0
            return True, "Symbol is set successfully."
        elif self.game_finished:
            # Send information to the losing player
            # and resets game
            winning_message = f"Player {self.winner_id} won! You lost, game reset!"
            self.reset_game()
            return False, winning_message 
        else:
            # Sends the winner the winning message
            self.game_finished = True
            self.winner_id = node_id
            return False, f"Player {self.winner_id} won!"

    def reset_game(self):
        """If the winner was found, restart"""
        # Send a request to the server to start the game

        self.game_finished = False
        self.board = [['-'] * self.board_size for _ in range(self.board_size)]  # 'empty' positions are marked as '-'

        print('Reseting the game')

        return True, f"Game was reset!"

    def manage_timeout(self, timeout=15):
        """
        The leader is also responsible to track and inforce time-outs
        in the systems. By default, if each player is idle for more than
         a minute, the game should reset back to its initial configuration.
         In addition, players could also inforce resetting the game.
         This however requires double verification, meaning that if both
         players haven’t heard a response from the server for about three
         minutes, they can reset the game.
        """
        print("Timer starts!")
        self.reset_time_counter = 0
        while self.reset_time_counter < timeout:
            if not self.timeout_happened:
                self.reset_time_counter += 1
                time.sleep(1)
                if self.reset_time_counter == timeout:
                    print("Timeout!")
                    self.reset_game()
                    self.reset_time_counter = 0
                    self.timeout_happened = True
        

    # returns board in a shape of matrix in a string format
    def list_board(self, node_id, args) -> str:
        """Show the board."""
        output_board_string = ''
        for i in range(self.board_size):
            for j in range(self.board_size):
                output_board_string += self.board[i][j] + '\t'
            output_board_string += '\n'
        return True, output_board_string

    def print_board(self, data):
        rows = data.split('\n')[:3]  # Split rows by newline
        for row in rows:
            cells = row.split('\t')[:4] # Split cells by tab
            print(f"\n{cells[0]}\t{cells[1]}\t{cells[2]}")
