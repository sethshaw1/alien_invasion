from typing import Any
import pygame
from pygame.sprite import Sprite

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, ss_game):
        "Create a bullet object at the player characters position"
        super().__init__()
        self.screen = ss_game.screen
        self.bullet_speed = 5.0
        self.bullet_colour = (0, 0, 0)
        self.bullet_height = 3
        self.bullet_width = 10
        
        # Create bullet rect at (0,0) then set correct postion
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)  
        self.rect.midleft = ss_game.player.rect.midleft
        self.rect.x += 110
        self.rect.y += 26
        # Store bullet position as a float
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet right across the screen"""
        # Update position of the bullet
        self.x += self.bullet_speed
        # Update rect postion
        self.rect.x = self.x
    
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.bullet_colour, self.rect)
    