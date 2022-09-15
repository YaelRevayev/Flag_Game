import pygame



def scatter_images():
    #initialize player

    #initialize flag

    #scatter grass
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0, 255, 0))
#scatter 20 grass pics

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                # Create a surface and pass in a tuple containing its length and width
                surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                # Give the surface a color to separate it from the background
                surf.fill((0, 0, 0))
                rect = surf.get_rect()
                screen.blit(surf, (0 , 0))
                pygame.display.flip()

                #show mokshim screen
        elif event.type == pygame.QUIT:
            running = False


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
