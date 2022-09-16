import pygame
import consts
import random
from time import time,sleep
from pygame.locals import *
from GridMatrix import GridMatrix

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
    pygame.display.set_caption('The Flag')
    screen.fill((34, 139, 34))
    scatter_images()
    text_objects()
    picture = pygame.transform.scale(pygame.image.load('pics_essential/flag.png'), (x * 4, y * 3))
    screen.blit(picture, consts.LEFT_CORNER_FLAG)
    picture = pygame.transform.scale(pygame.image.load('pics_essential/soldier.png'), (x * 2, y * 4))
    screen.blit(picture, (0, 0))

    pygame.display.flip()


def display_hidden_matrix():
    hidden_surface = pygame.Surface((1000, 500))
    hidden_surface.fill(consts.BLACK)
    for x in range(0, consts.SCREEN_WIDTH, int(consts.square_width)):
        for y in range(0, consts.SCREEN_LENGTH, int(consts.square_length)):
            rect = pygame.Rect(x, y, int(consts.square_width), int(consts.square_length))
            pygame.draw.rect(hidden_surface, consts.LIME_GREEN, rect, 1)


    screen.blit(hidden_surface, (0, 0))
    picture = pygame.transform.scale(pygame.image.load('pics_essential/soldier_nigth.png'),
                                     (consts.square_width * 2, consts.square_length * 4))
    screen.blit(picture, (0, 0))
    scan_for_traps()
    pygame.display.flip()


#example essential to display trap
def scan_for_traps():
    # scan grid matrix
    for i in range(len(grid_matrix)):
        j = 0
        while j < (consts.COLUMNS_MATRIX - 3):
            if grid_matrix[i][j] == "trap":
                show_trap_dark_mode(i, j)
                j += 3
            else:
                j += 1

def show_trap_dark_mode(i, j):
        #gets coordinate of first out of free squares trap
        #example:
        # (2,4)(2,5)(2,6) == trap in matrix
        # display_hidden_matrix(2,4)
    picture = pygame.transform.scale(pygame.image.load('pics_essential/mine.png'),
                                         (consts.square_width *3, consts.square_length * 1))
    screen.blit(picture, (consts.square_width * j, consts.square_length * i))
        #pygame.display.flip()

grid_matrix= GridMatrix().get_matrix()
normal_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                    display_hidden_matrix()
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


