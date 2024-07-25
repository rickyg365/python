import os
import pygame


def main():

    return

if __name__ == "__main__":
    # main()
    pygame.init()
    
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    run = True
    while run:
        # Event Handler
        for event in pygame.event.get():
            # Exit
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


