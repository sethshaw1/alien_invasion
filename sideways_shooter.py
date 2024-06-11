import sys
import pygame
from player import Player
from side_bullet import Bullet

class SidewaysShooter:
    """Overall class to generate the game"""
    
    def __init__(self):
        """Initialise the game, and create game resources"""
        # Initialise pygame background settings
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways Scroller")
        # Set the background colour
        self.bg_colour = (230, 230, 230)
        self.clock = pygame.time.Clock()
        
        self.bullet_fired = False
        self.reloading = False
        self.bullets_shot = 0
        
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            # Redraw the screen each pass through the loop
            self._check_feet_animations()
            self._check_animations()
            self.player.move()
            self._update_bullets()
            # Make the most recently drawn screen visible
            self._update_screen()
            self.clock.tick(30)
            
    def _update_screen(self):
        self.screen.fill(self.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.player.blitme()
        pygame.display.flip()
    
    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.QUIT:
                sys.exit()
    
    def _check_keydown(self, event):
        if event.key == pygame.K_q:
                    sys.exit()
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True 
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_DOWN:
            self.player.moving_down = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if not self.bullet_fired:
            if self.bullets_shot < 5:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
                self.bullet_fired = True
                self.bullets_shot += 1 
            elif self.bullets_shot == 5:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
                self.bullet_fired = True
                self.bullets_shot += 1 
                self.reloading = True
            else:
                self.reloading = True
            
    def _check_animations(self):
        if self.bullet_fired:
            self.player.shoot_update()
        elif self.reloading:
            self.player.reload_update()
        else:
            self.player.idle_update()
            
    def _check_feet_animations(self):
        if self.player.moving_up:
            self.player._strafe_left_update()
        elif self.player.moving_down:
            self.player._strafe_right_update()
        else:
            self.player.feet_image = self.player.idle_feet
            

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.player.screen_rect.right:
                self.bullets.remove(bullet) 
        print(len(self.bullets))
        
if __name__ == "__main__":
    ss = SidewaysShooter()
    ss.run_game()