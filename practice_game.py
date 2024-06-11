import sys
import pygame
from sprite import Sprite

class PracticeGame:
    """Overall class to create game for practice problems"""
    
    def __init__(self):
        """Create the function that initalises the game and creates the game
        resources"""
        pygame.init() # Function initalises the background settings that pygame needs
                  # to work properly.
    
        self.screen = pygame.display.set_mode((1000,600)) # Call set_mode function
                                                      # to set the size of the game
                                                      # window. Assign this to 
                                                      # variable self.screen so it
                                                      # is available to all methods
                                                      # in this class.
                                                      
        pygame.display.set_caption("Practice Game") #Sets the name of the game window
        
        self.knight = Sprite(self)
        
        self.bg_colour = (0, 0, 255) # Set the background colour (blue!)
        
    def run_game(self):
        while True:
            self._check_events()
            self.knight.update()
            self.screen.fill(self.bg_colour)
            self.knight.blitme()
            pygame.display.flip()
    
    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)     
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.knight.moving_right = True
        elif event.key == pygame.K_LEFT:
             # Move ship to the left
            self.knight.moving_left = True 
        elif event.key == pygame.K_UP:
            # Move ship up
            self.knight.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.knight.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()  
                    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.knight.moving_left = False
        elif event.key == pygame.K_UP:
            # Move ship up
            self.knight.moving_up = False
        elif event.key == pygame.K_DOWN:
            # Move ship down
            self.knight.moving_down = False

if __name__ == '__main__':
    """Creates an instance of the game and calls the run_game() function from 
    the PracticeGame class."""
    pg = PracticeGame()
    pg.run_game()