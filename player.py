class Player:
    """Class for implementing the tictactoe player."""

    def __init__(self, node_id, symbol):
        self.node_id = node_id
        self.symbol = symbol

    def set_symbol(self, position):
        """Set the request to set the symbol at particular location."""
        pass

    def list_board(self):
        """Send a request to show the board."""
        pass
