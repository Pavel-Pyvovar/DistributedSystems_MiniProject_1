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
            response = stub.SetSymbolCoordinator(tictactoe_pb2.SetSymbolCoordinatorRequest())
            print(f"Request from node {response.node_id} accepted.")
            # sends result info to server inside the function
            response = self.add_symbol(response.node_id, response.symbol, response.position, stub)
            if response.success:
                print("Player is successfuly notified about the result.")
            else:
                print("Player is not notified about the result.")



    def add_symbol(self, node_id, symbol, position, stub):
        if self.next_move_id.queue[0] != node_id:
            return stub.SetSymbolCoordinatorResult(
                tictactoe_pb2.SetSymbolCoordinatorResultRequest(
                    success=False, message="Is it not your turn."))

        if self.board[position[0]][position[1]] != '-':
            return stub.SetSymbolCoordinatorResult(
                tictactoe_pb2.SetSymbolCoordinatorResultRequest(
                    success=False, message="This position is already taken."))

        self.board[position[0]][position[1]] = symbol
        print(f"Symbol {symbol} is added from player {node_id}.")

        # switching the queue
        self.next_move_id.put(self.next_move_id.get())
        return stub.SetSymbolCoordinatorResult(
            tictactoe_pb2.SetSymbolCoordinatorResultRequest(
                success=True, message="Symbol is set successfully."))

    def reset_game(self):
        """If the winner was found, restart"""
        # Send a request to the server to start the game
        pass

    def manage_timeout(self):
        """
        The leader is also responsible to track and inforce time-outs
        in the systems. By default, if each player is idle for more than
         a minute, the game should reset back to its initial configuration.
         In addition, players could also inforce resetting the game.
         This however requires double verification, meaning that if both
         players haven’t heard a response from the server for about three
         minutes, they can reset the game.
        """
        pass

    # returns board in a shape of matrix in a string format
    def list_board(self) -> str:
        """Send a request to show the board."""
        output_board_string = ''
        for i in range(self.board_size):
            for j in range(self.board_size):
                output_board_string += self.board[i][j] + '\t'
            output_board_string += '\n'
        return output_board_string
