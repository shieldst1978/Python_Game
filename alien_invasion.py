import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
     
    def __init__(self):
        """Initialise the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # Set background colour
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            # Redraw the screen during each pass through the loop
            self._update_screen()                    
            self.clock.tick(60)

    def _check_events(self):
        # respond to keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RIGHT:
                        # Move the ship right
                        self.ship.rect.x += 1
                        

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        pygame.display.flip()
         

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()