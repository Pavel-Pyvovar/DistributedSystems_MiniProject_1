class GameCoordinator:
    """Leader that is responsible for managing the tictactoe game"""

    def __init__(self, leader_id, board, player_ids):
        self.leader_id = leader_id
        self.board = board
        self.player_ids = player_ids

    def check_winner(self):
        """Decide if there is a winner"""
        # This function probably should be called after every move
        # of any player to see if any row/column/diagonal is filled
        # with the same symbol
        pass

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

    def list_board(self):
        """Send a request to show the board."""
        pass