# Levi Baguley
# 5/25/18
# This file contains the Mitt class. It creates a curved polygon in the bottom center of the screen
# and allows the user to move it in a circular path with the mitt facing the center.
# There are 3 methods of this class. One finds the x and y components of the location of the mitt
# using a user-mutable angle attribute of the mitt and a parametric equation. The second turns the
# mitt to an angle based on mitts position angle to have the mitt face the center of the circle.
# The last makes the mitt appear at its correct position.


import math as m
import pygame as pg
from pygame.sprite import Sprite


class Mitt(Sprite):

    def __init__(self, settings, screen):
        """initialize the mitt and set its starting position"""
        super(Mitt, self).__init__()
        self.screen = screen
        self.settings = settings

        # create the mitt's image and get it's rect
        self.orig_img = pg.Surface((100, 15)).convert_alpha()
        self.orig_img.fill((0, 0, 0, 0))
        pg.draw.polygon(self.orig_img, (0, 0, 0),
                        [(0, 0), (8, 10), (40, 15), (60, 15), (92, 10), (100, 0), (40, 5), (60, 5)])
        self.rect = self.orig_img.get_rect()
        self.screen_rect = screen.get_rect()

        # starts each new mitt at the bottom of the circular path
        self.path_radius = (self.settings.screen_height / 2) - 20
        self.rect.centerx = self.screen_rect.centerx + self.path_radius * m.cos(m.pi / 2)
        self.rect.centery = self.screen_rect.centery + self.path_radius * m.sin(m.pi / 2)
        self.theta = m.pi / 2
        self.mitt_angle = 0

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the mitt's position based on movement flags"""
        # update the mitt's center value by using changing theta and using theta in a parametric equation.
        if self.moving_right:
            self.theta -= self.settings.mitt_speed

            self.rect.centerx = self.screen_rect.centerx + self.path_radius * m.cos(self.theta)
            self.rect.centery = self.screen_rect.centery + self.path_radius * m.sin(self.theta)

        if self.moving_left:
            self.theta += self.settings.mitt_speed

            self.rect.centerx = self.screen_rect.centerx + self.path_radius * m.cos(self.theta)
            self.rect.centery = self.screen_rect.centery + self.path_radius * m.sin(self.theta)

    def turn_mitt(self):
        """turns mitt to an angle based on mitts position angle to have mitt face center of circle"""
        self.mitt_angle = -(self.theta - m.pi / 2) * 180 / m.pi

        # takes original image and rotates it
        self.image = pg.transform.rotozoom(self.orig_img, self.mitt_angle, 1)

        # makes new rect from new rotated image and center
        self.rect = self.image.get_rect(center=self.rect.center)

    def blitme(self):
        """draw the mitt"""
        self.screen.blit(self.image, self.rect)
