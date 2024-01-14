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
    pygame.display.set_caption("Game in Progress")
    
    # Player
    X = 50
    Y = 50
    W = 50
    H = 50
    V = 5

    player = pygame.Rect((X, Y, W, H))
    
    # Game Loop
    run = True
    while run:
        # Clock?
        pygame.time.delay(100)

        # Fill/refresh screen
        screen.fill((0, 0, 0))

        # Event Handler
        for event in pygame.event.get():
            # Exit
            if event.type == pygame.QUIT:
                run = False

        # Controls
        key = pygame.key.get_pressed()

        if key[pygame.K_a] == True:
            # print("a")
            player.move_ip(-V, 0)  # Move in place
        elif key[pygame.K_d] == True:
            # print("d")
            player.move_ip(V, 0)  # Move in place
        elif key[pygame.K_s] == True:
            # print("s")
            player.move_ip(0, V)  # Move in place
        elif key[pygame.K_w] == True:
            # print("w")
            player.move_ip(0, -V)  # Move in place

        # Draw to player screen
        pygame.draw.rect(screen, (255, 0, 0), player)  # screen, rgb, Rect

        # Update Display
        pygame.display.update()


    pygame.quit()


