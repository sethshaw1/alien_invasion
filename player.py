import pygame
from pathlib import Path

class Player(pygame.sprite.Sprite):
    """Class to manage the gunman sprite"""
    
    def __init__(self, ss_game):
        """Initialise the player and set starting postion"""
        super().__init__()
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.bullet_fired = ss_game.bullet_fired
        self.reloading = ss_game.reloading
        
        # Load the animation images
        self._load_idle_images()
        self._load_reload_images()
        self._load_shoot_images()
        self._load_feet_idle()
        self._load_strafe_left()
        self._load_strafe_right()
        
        # Set the initial player body image and get it's rect
        self.current_sprite = 0
        self.image = self.idle[self.current_sprite]
        self.rect = self.image.get_rect()
        
        # Set the players initial foot image and get it's rect
        self.current_feet = 0
        self.feet_image = self.idle_feet
        self.feet_rect = self.feet_image.get_rect()
        
        # Start the player at the middle left of the screen
        self.rect.midleft = self.screen_rect.midleft
        self.feet_rect.midleft = self.screen_rect.midleft
        
        # Set movement flags to false
        self.moving_up = False
        self.moving_down = False
    
    def idle_update(self):
        self.current_sprite += 0.2 
        if self.current_sprite >= len(self.idle):
            self.current_sprite = 0
        self.image = self.idle[int(self.current_sprite)]
    
    def shoot_update(self):
        self.current_sprite += 1.5
        if self.current_sprite >= len(self.shoot):
            self.ss_game.bullet_fired = False
            self.current_sprite = 0
        self.image = self.shoot[int(self.current_sprite)]
        
    def reload_update(self):
        self.current_sprite += 0.4
        if self.current_sprite >= len(self.reload):
            self.current_sprite = 0
            self.ss_game.bullets_shot = 0
            self.ss_game.reloading = False
        self.image = self.reload[int(self.current_sprite)]
        
    def _strafe_left_update(self):
        self.current_feet += 1
        if self.current_feet >= len(self.strafe_left):
            self.current_feet = 0
        self.feet_image = self.strafe_left[int(self.current_feet)]
    
    def _strafe_right_update(self):
        self.current_feet += 1
        if self.current_feet >= len(self.strafe_right):
            self.current_feet = 0
        self.feet_image = self.strafe_right[int(self.current_feet)]
        
    def move(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 4
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 4
            
    def _load_idle_images(self):
        # Load the player idle images 
        self.idle = []
        for i in range(0, 19):
            self.idle.append(pygame.transform.scale_by(pygame.image.load(
                f'images/Top_Down_Survivor/handgun/idle/survivor-idle_handgun_{i}.png'), 0.5))
        
    def _load_reload_images(self):
        # Load reload images 
        self.reload = []
        for i in range(0, 14):
            self.reload.append(pygame.transform.scale_by(pygame.image.load(
                f'images/Top_Down_Survivor/handgun/reload/survivor-reload_handgun_{i}.png'), 0.5))
        
    def _load_shoot_images(self):
        # Load shoot images 
        self.shoot = []
        for i in range(1, 22):
            self.shoot.append(pygame.transform.scale_by(pygame.image.load(
                f'images/Top_Down_Survivor/handgun/shoot/survivor-shoot_handgun_{i}.png'), 0.5))
    
    def _load_feet_idle(self):
        # Load idle feet image 
        self.idle_feet = pygame.transform.scale_by(pygame.image.load(
            'images/Top_Down_Survivor/feet/idle/survivor-idle_0.png'), 0.5)
    
    def _load_strafe_left(self):
        self.strafe_left = []
        for i in range(0, 19):
            self.strafe_left.append(pygame.transform.scale_by(pygame.image.load(
                f'images/Top_Down_Survivor/feet/strafe_left/survivor-strafe_left_{i}.png'), 0.5))
    
    def _load_strafe_right (self):
        self.strafe_right = []
        for i in range(0, 19):
            self.strafe_right.append(pygame.transform.scale_by(pygame.image.load(
                f'images/Top_Down_Survivor/feet/strafe_right/survivor-strafe_right_{i}.png'), 0.5))
        
        
    def blitme(self):
        """Draw player at current location"""
        # Draw feet
        self.feet_rect.center = self.rect.center
        self.screen.blit(self.feet_image, self.feet_rect)
        # Draw body on feet
        self.screen.blit(self.image, self.rect)
    