class Move:
    def __init__(self, i, board_code, recommendations, player):
        self.position = i
        self.board_code = board_code
        self.recommendations = recommendations
        self.player = player
