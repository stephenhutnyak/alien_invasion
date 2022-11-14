# This is our settings module

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 255, 255)

        # Star settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
