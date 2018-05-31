# -*- coding:utf-8 -*-

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/font.ttf', 25)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_lives()
        self.draw_line()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("SCORE : " + score_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render( "HIGH SCORE : " + high_score_str, True,
            self.text_color, self.ai_settings.bg_color)
                
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render( "LEVEL : " + str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.top

    def prep_lives(self):
        self.lives = self.font.render("LIVES : ", True,
                                          self.text_color, self.ai_settings.bg_color)
        # Position the level below the score.
        self.lives_rect = self.lives.get_rect()
        self.lives_rect.x = 10
        self.lives_rect.y = 760

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 120 + ship_number * ship.rect.width
            ship.rect.y = 750
            self.ships.add(ship)


    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives, self.lives_rect)
        # Draw ships.
        self.ships.draw(self.screen)

    def draw_line(self):
        pygame.draw.line(self.screen, (0, 255, 0), (0, 740), (1280, 740), 3)
