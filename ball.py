# Levi Baguley
# 5/25/18
# This file contains the Ball class. It creates a black circle in the center of the screen and stores its mutable
# location. There are 2 methods of this class. One finds the x and y components of a random direction vector using a
# random angle attribute of the ball. The other makes the ball appear at its correct position.

import random
import math as m
import pygame as pg
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to represent a ball to catch"""

    def __init__(self, settings, screen):
        """Initialize the ball and set its starting position"""
        super(Ball, self).__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # render the ball image and set its rect
        self.image = pg.Surface((20, 20)).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, (0, 0, 0), (10, 10), 10)
        self.rect = self.image.get_rect()

        # start each new ball in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # holds the origin of the ball in the center of the screen(constant)
        self.originx = self.screen_rect.centerx
        self.originy = self.screen_rect.centery

        # attribute to hold store ball's exact position (float)
        self.ball_xpos = self.screen_rect.centerx
        self.ball_ypos = self.screen_rect.centery

        # Initialize the ball's random angle, direction radius and direction vector
        self.random_angle = random.uniform(0, 2 * m.pi)
        self.path_radius = (self.settings.screen_height / 2) - 20
        self.vect_x = 0
        self.vect_y = 0

    def find_direction(self):
        """find a random direction for the ball to be thrown using the ball's random angle"""
        # chooses a random point along the circular path
        random_x = self.originx + self.path_radius * m.cos(self.random_angle)
        random_y = self.originy + self.path_radius * m.sin(self.random_angle)

        """find direction vector <self.vect_x, self.vect_y> between the ball (in the center) and random point"""
        # find the vector <dx, dy> from center to random point
        dx = random_x - self.originx
        dy = random_y - self.originy
        # find magnitude of <dx, dy> vector
        mag = m.sqrt(dx ** 2 + dy ** 2)
        # normalize <dx, dy> to find a unit direction vector
        self.vect_x = dx / mag
        self.vect_y = dy / mag

    def blit_me(self):
        """makes the ball appear at its current position"""
        self.screen.blit(self.image, self.rect)
