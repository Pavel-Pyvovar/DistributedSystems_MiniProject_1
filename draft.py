# leader election depends on server and client architechture, leave it for later
# request acceptance and reply also depends on the same + .proto architechtire -> finish these parts while merging

# with each request and reply send timestamps!


class LeaderNode:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.commands_dispatch = {
                                     "Set-symbol": self.set_symbol,
                                     "List-board"L self.list_board,
                                 "Set-node-time": self.set_node_time
        }
        self.board = [['-'] * self.board_size for _ in range(self.board_size)]  # 'empty' positions are marked as '-'
        self.symbols = {'O': False, 'X': False}  # is assigned

    # assigning symbols
    def assign_symbol(self):
        # need to read client id and send him back his symbol, aka reply.symbol = '..'
        pass

        # set symbol to a board by position

    def set_symbol(self, symbol, position):  # do we do matrix-alike position?
        self.board[position[0]][position[1]] = symbol
        # need to read client id and send him back his symbol, aka reply.symbol = '..'
        pass

    # visualizing current board state
    def list_board(self):  # tested
        output_board_string = ''
        for i in range(self.board_size):
            for j in range(self.board_size):
                output_board_string += self.board[i][j] + '\t'
            output_board_string += '\n'
        return output_board_string

    def start_game(self):
        # exit when there is a winner
        while True:
            # accept request

            # assume that the command is stored in the 'command' variable, then to execute it
            #
            # command_name = request.command
            # command_arguments = request.arguments        # can be sent as a string and then parsed? depends on .proto implementation
            # request.reply = self.commands_dispatch[request.command]([command_argument1, command_argument2])
            #
            # all master node text answers are stored in the 'reply' string variable

            if self.check_winner_combination() == '-':
            # do next step of commands aka send reply to requests

            pass

    def check_winner_combination(self):  # tested
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


if __name__ == '__main__':
    pass
