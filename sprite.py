import pygame

class Sprite:
    """Class to manage the knight game sprite"""
    
    def __init__(self, pg_game): # Name of argument pg_game is arbitary, self.knight
                                 # passes self as this arg to give information
        self.screen = pg_game.screen
        self.screen_rect = pg_game.screen.get_rect()
        
        self.image = pygame.image.load('images/onlyrocket.bmp')
        self.image = pygame.transform.scale(self.image, (100, 300))
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center 
        
        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        self.y =float(self.rect.y)
        
        # Movement flags, starts not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update position of the sprite based on movement flags"""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 2
        if self.moving_left and self.rect.left > 0:
            self.x -= 2
        if self.moving_up and self.rect.top > 0:
            self.y -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 2
        
        # Update the rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)