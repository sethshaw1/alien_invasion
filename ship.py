import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game): # init method of Ship takes 2 parameters, the 
                                 # self reference and a reference to the current
                                 # instance of the Alien Invasion class. This 
                                 # gives ship access to all the resources in 
                                 # Alien Invasion
                                
        """Init ship and set starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        
        # Movement flags, starts not moving
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update ship's position based on the movement flag"""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update the rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location
        """
        self.screen.blit(self.image, self.rect)