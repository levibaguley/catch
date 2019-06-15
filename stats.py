# Levi Baguley
# 5/25/18
# This file contains the Stats class. It initializes the statistics of the game including the number of lives and the
# score it also initializes the flags that say if the game is active and if a game over loop should continue.


class Stats:
    """stats of number of lives and number of balls caught"""

    def __init__(self):
        """Initialize statistics"""
        self.reset_stats()

    def reset_stats(self):
        """initialize stats"""
        self.lives = 3
        self.score = 0
        self.game_active = True
        self.game_over = True
