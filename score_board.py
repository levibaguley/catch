# Levi Baguley
# 5/25/18
# This file contains the Scoreboard class. It initializes different font settings that will be
# used to display information to the user. The methods of this class render images of the number of lives the player
# has and their current score, and draws them to the screen. Two other methods create and display images that tell
# the player that the game is over and tells them how to play again. This class also contains a method that resets
# the font settings that can change during the game.

import pygame.font
import pygame


class Scoreboard:
    """A class to display scoring, game loss and the option to play again"""

    def __init__(self, settings, screen, stats):
        """Initialize score attributes including font settings"""
        # variables to pass
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # font settings for scoring
        self.text_color = (0, 0, 0)
        self.font_size = 40
        self.font = pygame.font.SysFont('monospace', self.font_size)

        # font settings for number of lives
        self.lives_color = (0, 0, 0)
        self.lives_text = "Lives:"

        # font settings for the 'Game over image'
        self.game_over_size = 110
        self.game_over_color = (173, 0, 0)
        self.game_over_font = pygame.font.SysFont('monospace', self.game_over_size)

        # prepare the initial score and lives images
        self.prep_score()
        self.prep_lives()

    def reset_lives_font(self):
        """reset dynamic font settings"""
        self.lives_color = (0, 0, 0)
        self.lives_text = "Lives:"

    def prep_score(self):
        """turn the score into a rendered image"""
        self.score_image = self.font.render("Score: " + str(self.stats.score), True, self.text_color,
                                            self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score and number of lives to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lives_image, self.lives_rect)

    def prep_lives(self):
        """Turns the number of lives into an image"""
        # if on the last life, changes image to "LAST LIFE!: 0" in red text
        if self.stats.lives <= 0:
            self.lives_text = "LAST LIFE!:"
            self.lives_color = (255, 0, 0)

        # makes lives image
        self.lives_image = self.font.render(self.lives_text + str(self.stats.lives), True, self.lives_color,
                                            self.settings.bg_color)

        # Position the number of lives below the score.
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.score_rect.right
        self.lives_rect.top = self.score_rect.bottom + 10

    def game_over(self):
        """Show "Game Over as an image"""
        # make 'Game over' image
        self.game_over_image = self.game_over_font.render("GAME OVER", True, self.game_over_color,
                                                          self.settings.bg_color)

        # Display in the center screen of the screen
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.settings.screen_center

        # Create outline and center dot
        pygame.draw.rect(self.screen, (0, 0, 0), self.game_over_rect, 5)
        self.screen.blit(self.game_over_image, self.game_over_rect)
        pygame.draw.circle(self.screen, self.settings.circle_color, self.settings.screen_center,
                           self.settings.inner_circle_radius, )

    def play_again_text(self):
        """Display the option to play again"""
        # make play_again image
        self.play_again_image = self.font.render("Press p to play again", True, self.text_color, self.settings.bg_color)

        # center image below 'game over'
        self.play_again_rect = self.play_again_image.get_rect()
        self.play_again_rect.center = self.settings.screen_center
        self.play_again_rect.centery += 100
        self.screen.blit(self.play_again_image, self.play_again_rect)
