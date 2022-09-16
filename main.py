import pygame
import consts
import random
from time import time,sleep
from pygame.locals import *
import sys

x=consts.square_width
y=consts.square_length

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))
def text_objects():
    pygame.font.init()
    font = pygame.font.SysFont('freesansbold.ttf',25,True,False)
    textSurface = font.render("Welcome To the Flag Game! \n "
                              " Have Fun ", False, (250, 250, 250))
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = (10*x,y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def scatter_images():
    for i in range(50):
        rand_x = random.uniform(0,consts.SCREEN_WIDTH)
        rand_y = random.uniform(0, consts.SCREEN_LENGTH)
        picture = pygame.transform.scale(pygame.image.load('pics_essential/grass.png'), (x * 2, y * 2))
        screen.blit(picture, (rand_x, rand_y))


def normal_screen(x_ind=x,y_ind=y):
    pygame.init()
    # Define constants for the screen width and height
    pygame.display.set_caption('The Flag')
    screen.fill((34, 139, 34))
    text_objects()
    picture = pygame.transform.scale(pygame.image.load('pics_essential/soldier.png'), (x * 2, y * 4))
    screen.blit(picture, (0, 0))
    scatter_images()
    pygame.display.flip()


def display_hidden_matrix():

    hidden_surface = pygame.Surface((1000, 500))
    hidden_surface.fill(consts.BLACK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, consts.SCREEN_WIDTH, int(consts.square_width)):
        for y in range(0, consts.SCREEN_LENGTH, int(consts.square_length)):
            rect = pygame.Rect(x, y, int(consts.square_width), int(consts.square_length))
            pygame.draw.rect(hidden_surface, consts.LIME_GREEN, rect, 1)
    return hidden_surface


normal_screen()
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                    screen.blit(display_hidden_matrix(), (0, 0))
                    pygame.display.flip()
                    sleep(1 - time() % 1)
                    normal_screen()
                    pygame.display.flip()
            if event.key == K_ESCAPE:
                pygame.display.flip()

        elif event.type == pygame.QUIT:
            running = False


    # Flip the display
    pygame.display.flip()


pygame.quit()


