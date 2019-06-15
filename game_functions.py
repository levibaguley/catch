# Levi Baguley
# 5/25/18

# This file contains several functions that are used throughout the game. These functions include: ball and mitt
# movement, creation and deletion. They also include screen updates and background creation. See comments below for
# more details

import sys
import pygame
from ball import Ball
from mitt import Mitt

from time import sleep


def check_keydown_events(event, settings, screen, mitt, stats):
    """respond to keypresses"""
    # changes mitts movement flags
    if event.key == pygame.K_RIGHT:
        mitt.moving_right = True
    elif event.key == pygame.K_LEFT:
        mitt.moving_left = True
    # ends the game over loop if user presses p
    elif event.key == pygame.K_p and not stats.game_active:
        stats.game_over = False


def check_keyup_events(event, mitt):
    """respond to key releases for mitt to stop"""
    if event.key == pygame.K_RIGHT:
        mitt.moving_right = False
    elif event.key == pygame.K_LEFT:
        mitt.moving_left = False


def check_events(settings, screen, mitt_group, stats):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        for mitt in mitt_group:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, settings, screen, mitt, stats)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, mitt)


def update_screen(settings, screen, mitt_group, ball_group, stats, sb):
    """update images on the screen and flip to the new screen"""
    # redraw the background first during each pass through the loop
    draw_background(settings, screen)

    # update mitt
    draw_mitt(mitt_group)

    # update ball
    move_ball(settings, screen, mitt_group, ball_group, stats, sb)
    for ball in ball_group:
        ball.blit_me()

    # check if ball was caught and updates score
    check_ball_caught(settings, screen, mitt_group, ball_group, stats, sb)
    sb.show_score()

    # make the most recently drawn screen visible
    pygame.display.flip()


def missed(ball_group):
    """checks if ball has been missed and hit the edge of the screen"""
    for ball in ball_group:
        if ball.rect.right >= ball.screen_rect.right:
            return True
        elif ball.rect.left <= 0:
            return True
        elif ball.rect.top <= 0:
            return True
        elif ball.rect.bottom >= ball.screen_rect.bottom:
            return True
        else:
            return False


def move_ball(settings, screen, mitt_group, ball_group, stats, sb):
    """ move ball unless missed then goes to next life"""
    # deletes if missed
    for ball in ball_group:
        if missed(ball_group):
            next_life(settings, screen, mitt_group, ball_group, stats, sb)

        # move along direction vector towards the random point at current ball speed
        else:
            ball.ball_xpos += ball.vect_x * ball.settings.ball_speed
            ball.ball_ypos += ball.vect_y * ball.settings.ball_speed
            # updates ball center position
            ball.rect.center = (ball.ball_xpos, ball.ball_ypos)


def check_ball_caught(settings, screen, mitt_group, ball_group, stats, sb):
    """checks if mitt caught ball"""
    # if caught deletes ball and adds to score
    caught = pygame.sprite.groupcollide(ball_group, mitt_group, True, False)
    if caught:
        create_ball(settings, screen, ball_group)
        stats.score += 1
        sb.prep_score()
        settings.speed_up()


def create_ball(settings, screen, ball_group):
    """creates a new ball in the center and chooses a random direction to go"""
    ball = Ball(settings, screen)
    ball_group.add(ball)
    ball.find_direction()


def create_mitt(settings, screen, mitt_group):
    """creates a new mitt at the bottom of the screen"""
    mitt = Mitt(settings, screen)
    mitt_group.add(mitt)


def draw_background(settings, screen):
    """draws the background color and circles"""
    screen.fill(settings.bg_color)
    pygame.draw.circle(screen, settings.circle_color, settings.screen_center, settings.inner_circle_radius, )
    pygame.draw.circle(screen, settings.circle_color, settings.screen_center, settings.circle_radius,
                       settings.circle_thickness)


def draw_mitt(mitt_group):
    """draws the mitt in its current location"""
    for mitt in mitt_group:
        mitt.update()
        mitt.turn_mitt()
        mitt.blitme()


def next_life(settings, screen, mitt_group, ball_group, stats, sb):
    """Goes on to next life if player has one"""
    if stats.lives >= 1:
        # deletes current ball and mitt and create new ones
        ball_group.empty()
        mitt_group.empty()
        create_ball(settings, screen, ball_group)
        create_mitt(settings, screen, mitt_group)

        # subtracts from number of lives, stops game for a moment
        stats.lives -= 1
        sb.prep_lives()
        sleep(0.5)

    # ends game if player loses all lives
    else:
        stats.game_active = False


def play_again(settings, screen, mitt_group, ball_group, stats, sb):
    """Start a new game"""
    # reset the game speed
    settings.reset_speed()

    # reset the game statistics
    stats.reset_stats()

    # reset the scoreboard images
    sb.prep_score()
    sb.reset_lives_font()
    sb.prep_lives()

    # delete ball and mitt and create a new ones
    mitt_group.empty()
    ball_group.empty()
    create_mitt(settings, screen, mitt_group)
    create_ball(settings, screen, ball_group)
