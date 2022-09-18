import pygame
import consts
import random
from time import time,sleep
from pygame.locals import *
from GridMatrix import GridMatrix
from Soldier import Player
import Soldier

x=consts.square_width
y=consts.square_length
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))

def text_objects():
    pygame.font.init()
    font = pygame.font.SysFont('freesansbold.ttf',25,True,False)
    textSurface = font.render("Welcome To the Flag Game! "
                              " Have Fun ", False, consts.WHITE)
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = (10*x,y)
    screen.blit(TextSurf, TextRect)
    pygame.display.flip()


def won_lost_text(txt):
    pygame.font.init()
    font = pygame.font.SysFont('freesansbold.ttf',30,True,False)
    textSurface = font.render(txt, False, consts.WHITE)
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = (consts.SCREEN_WIDTH/2,consts.SCREEN_LENGTH/2)
    screen.blit(TextSurf, TextRect)
    pygame.display.flip()


def scatter_images():
    for i in range(50):
        rand_x = random.uniform(0,consts.SCREEN_WIDTH)
        rand_y = random.uniform(0, consts.SCREEN_LENGTH)
        picture = pygame.transform.scale(pygame.image.load('pics_essential/grass.png'), (x * 2, y * 2))
        screen.blit(picture, (rand_x, rand_y))
    pygame.display.flip()


def normal_screen(player,x_ind=x,y_ind=y):
    pygame.init()
    pygame.display.set_caption('The Flag')
    screen.fill((34, 139, 34))
    scatter_images()
    text_objects()
    picture = pygame.transform.scale(pygame.image.load('pics_essential/flag.png'), (x * 4, y * 3))
    screen.blit(picture, consts.LEFT_CORNER_FLAG)
    display_soldair(player)
    pygame.display.update()


def display_soldair(player):
    picture = pygame.transform.scale(pygame.image.load('pics_essential/soldier.png'), (x * 2, y * 4))
    screen.blit(picture, (x*player.get_j_leftcorner(),y*player.get_i_leftcorner()))
    pygame.display.update()


def display_hidden_matrix(player):
    hidden_surface = pygame.Surface((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))
    hidden_surface.fill(consts.BLACK)
    for x in range(0, consts.SCREEN_WIDTH, int(consts.square_width)):
        for y in range(0, consts.SCREEN_LENGTH, int(consts.square_length)):
            rect = pygame.Rect(x, y, int(consts.square_width), int(consts.square_length))
            pygame.draw.rect(hidden_surface, consts.LIME_GREEN, rect, 1)

    picture = pygame.transform.scale(pygame.image.load('pics_essential/soldier_nigth.png'),
                                     (consts.square_width * 2, consts.square_length * 4))
    hidden_surface.blit(picture, (player.get_j_leftcorner()*consts.square_width,
                          player.get_i_leftcorner()* consts.square_length))
    screen.blit(hidden_surface, (0, 0))
    scan_for_traps()
    pygame.display.flip()
    sleep(1 - time() % 1)


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


def handle_event(i_change=0,j_change=0):
    list_o_tuples = Soldier.calc_body_indexes(player.get_i_leftcorner() + i_change,
                                              player.get_j_leftcorner()+j_change)
    if Soldier.tuples_in_borders(list_o_tuples):
        player.set_i_leftcorner(player.get_i_leftcorner() + i_change)
        player.set_j_leftcorner(player.get_j_leftcorner()+j_change)
        normal_screen(player)

# ------------------main screen event handling------------------
grid_object=GridMatrix()
grid_matrix= grid_object.get_matrix()
player=Player()
normal_screen(player)
display_soldair(player)
running = True

while running:
    if player.check_touch_flag(grid_matrix):
        won_lost_text("You Won!")
        sleep(3 - time() % 3)
        running = False

    # player won---> running=False
    if player.check_touch_trap(grid_object):
        won_lost_text("You Lost!")
        sleep(3 - time() % 3)
        running = False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key==pygame.K_DOWN:
                handle_event(i_change=1)

            if event.key==pygame.K_UP:
                handle_event(i_change=-1)

            if event.key==pygame.K_LEFT:
                handle_event(j_change=-1)

            if event.key==pygame.K_RIGHT:
                handle_event(j_change=1)

            if event.key == pygame.K_RETURN:
                    display_hidden_matrix(player)
                    normal_screen(player)

            if event.key == K_ESCAPE:
                pygame.display.flip()

        elif event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()

pygame.quit()


