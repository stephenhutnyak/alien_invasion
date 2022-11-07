import sys

import pygame

class GameTime:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Game Time")
        self.bg_color = (0, 255, 255)

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = GameTime()
    ai.run_game()