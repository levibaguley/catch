# Levi Baguley
# 5/25/18

# This file contains the Settings class. It initializes different font settings that will be used throughout the game
# and is used as a convenient way for a programmer to change the settings. These settings relate to screen size,
# color and background. The class also contains speed settings. The two methods of this class increase the mitt and
# speed settings according to a speed-up scale, and reset the speed.

import math as m


class Settings:
    """ A Class to store all settings for Catch"""

    def __init__(self):
        """initialize the games settings"""
        # screen settings
        self.screen_width = 1300
        self.screen_height = 650
        self.screen_center = (int(self.screen_width / 2), int(self.screen_height / 2))
        self.circle_radius = int((650 / 2) - 20)
        self.bg_color = (255, 255, 255)

        # settings of background circle and center dot
        self.circle_radius = int((self.screen_height / 2) - 20)
        self.circle_thickness = 1
        self.inner_circle_radius = 3
        self.circle_color = (0, 0, 0)

        # ball and mitt speed settings
        self.mitt_speed = (m.pi / 1000)
        self.ball_speed = .2

        # speed up scale
        self.speed_up_scale = 1.05

    def speed_up(self):
        """speeds up mitt and ball"""
        self.mitt_speed *= self.speed_up_scale
        self.ball_speed *= self.speed_up_scale

    def reset_speed(self):
        """resets speed"""
        self.mitt_speed = (m.pi / 1000)
        self.ball_speed = .2
