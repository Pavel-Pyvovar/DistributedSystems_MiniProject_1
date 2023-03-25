import tictactoe_pb2


class Player:
    """Class for implementing the tictactoe player."""

    def __init__(self, node_id, symbol):
        self.node_id = node_id
        self.symbol = symbol

    def set_symbol(self, stub, position):
        """Set the request to set the symbol at particular location."""
        return stub.SetSymbolPlayer(
            tictactoe_pb2.SetSymbolPlayerRequest(
                node_id=self.node_id, symbol=self.symbol, position=position))


    def list_board(self):
        """Send a request to show the board."""
        pass
