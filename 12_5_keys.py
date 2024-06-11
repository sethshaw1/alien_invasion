import sys 
import pygame

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Keys")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.type)
                    print(event.key)
            pygame.display.flip()

if __name__ == '__main__':
    k = Keys()
    k.run_game()
    