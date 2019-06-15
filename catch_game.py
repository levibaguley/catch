# Levi Baguley
# 5/25/18
# This is the run game file of a 2D game in which the player controls a 'mitt' that moves in a
# circular path. A 'ball' appears in the center of the circle and moves in a random direction. Only one ball is on
# the screen at a time. The player must 'catch' the ball before it goes out side of the circle. Every time the ball
# is caught a point is given and the game speeds up. If the ball is missed the mitt returns to the bottom of the
# screen and a life is taken away. The player has 3 lives. If the player loses all of their lives they are given an
# option to play again. If they choose to do so the game resets and starts over from the beginning.

import pygame
from pygame.sprite import Group

from settings import Settings
from stats import Stats
from score_board import Scoreboard
from mitt import Mitt
import game_functions as gf


def run_game():
    # Initialize pygame, settings and screen
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catch")

    # Initialize stats and scoreboard
    stats = Stats()
    sb = Scoreboard(settings, screen, stats)

    # make a mitt
    mitt = Mitt(settings, screen)
    mitt_group = Group(mitt)

    # make a group to hold all balls during game
    ball_group = Group()

    # make the first ball of the game
    gf.create_ball(settings, screen, ball_group)

    # Start the main loop
    while True:
        # game active loop
        while stats.game_active:
            gf.check_events(settings, screen, mitt_group, stats)
            gf.update_screen(settings, screen, mitt_group, ball_group, stats, sb)

        # game over loop
        while stats.game_over:
            gf.check_events(settings, screen, mitt_group, stats)
            sb.game_over()
            sb.play_again_text()
            pygame.display.flip()

        # play again set up
        gf.play_again(settings, screen, mitt_group, ball_group, stats, sb)


run_game()
