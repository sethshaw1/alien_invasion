import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_game):
        """Initialise the alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        
        # Load alien image and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store aliens exact horizontal position
        self.x = float(self.rect.x)