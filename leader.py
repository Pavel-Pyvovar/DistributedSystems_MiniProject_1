class GameCoordinator:
    """Leader that is responsible for managing the tictactoe game"""

    def __init__(self, leader_id, player_ids_symbols: dict, board_size=3):
        self.leader_id = leader_id  # check if we need it
        # i think should be initialized here, not from outside
        self.board_size = board_size
        self.board = [['-'] * self.board_size for _ in range(self.board_size)]  # 'empty' positions are marked as '-'
        self.player_ids_symbols = player_ids_symbols

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
