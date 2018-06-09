import pygame
import os

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        # Ship settings.
        self.ship_limit = 2
        self.have_sound = True
            
        # Bullet settings.
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 10
            
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5
        # Pasue
        self.game_pause = False
    
        self.initialize_dynamic_settings()
        self.initialize_sound_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        if (os.name == 'posix'):
            self.ship_speed_factor = 6.0
            self.bullet_speed_factor = 12
            self.alien_speed_factor = 100
        else:
            self.ship_speed_factor = 1.5
            self.bullet_speed_factor = 3
            self.alien_speed_factor = 1
        
        # Scoring.
        self.alien_points = 50
    
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def initialize_sound_settings(self):
        try:
            self.shot_sound = pygame.mixer.Sound('sounds/shoot.wav')
            self.alien_die_sound = pygame.mixer.Sound('sounds/invaderkilled.wav')
            self.die_sound = pygame.mixer.Sound('sounds/explosion.wav')

            #Play Background Music
            pygame.mixer.music.load("sounds/music.mp3")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(loops=1)
        except pygame.error as e:
            print ("Can't load sound effects")
            self.have_sound = False

        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)

