import pygame
import consts
from time import time,sleep
from pygame.locals import *
from GridMatrix import GridMatrix
from Soldier import Player
import Soldier
import keyboard
import DateBase
import ctypes
x=consts.square_width  # wodth (in pixels) of one square in our matrix
y=consts.square_length  # length (in pixels) of one square in our matrix
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))

def text_objects():
    #displays on screen welcome text when function is called
    pygame.font.init()
    font = pygame.font.SysFont('freesansbold.ttf',25,True,False)
    textSurface = font.render("Welcome To the Flag Game! "
                              " Have Fun ", False, consts.WHITE)
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = (10*x,y)
    screen.blit(TextSurf, TextRect)
    pygame.display.flip()


def won_lost_text(txt):
    # displays txt-string paramter on the center
    # of the screen when functions is called
    pygame.font.init()
    font = pygame.font.SysFont('freesansbold.ttf',30,True,False)
    textSurface = font.render(txt, False, consts.WHITE)
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = (consts.SCREEN_WIDTH/2,consts.SCREEN_LENGTH/2)
    screen.blit(TextSurf, TextRect)  # put the object on screen and updates
    pygame.display.flip()


def scatter_grass():
    # displays random grass objects on screen when called
    parallel_grass_grid=helpful_grid_grass.get_matrix()
    for i in range(len(parallel_grass_grid)):
        for j in range(len(parallel_grass_grid[i])):
            if parallel_grass_grid[i][j]=="grass":
                picture = pygame.transform.scale(pygame.image.load('pics_essential/grass.png'), (x * 2, y * 2))
                screen.blit(picture, (j*x, i*y))
    pygame.display.flip()


def normal_screen(player,x_ind=x,y_ind=y):
    # displays welcome text + garss images + soldier
    # at his recent position in matrix
    pygame.init()
    pygame.display.set_caption('The Flag')
    screen.fill((34, 139, 34))
    scatter_grass()
    text_objects()
    picture = pygame.transform.scale(pygame.image.load('pics_essential/flag.png'), (x * 4, y * 3))
    screen.blit(picture, consts.LEFT_CORNER_FLAG)
    display_soldair(player)
    pygame.display.update()


def display_soldair(player):
    # using features of the player object to display the image on the screen
    picture = pygame.transform.scale(pygame.image.load('pics_essential/soldier.png'), (x * 2, y * 4))
    screen.blit(picture, (x*player.get_j_leftcorner(),y*player.get_i_leftcorner()))
    pygame.display.update()


def display_hidden_matrix(player):
    # shows a surface of dark matrix screen with traps
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
    # scans grid matrix for the first square of each trap
    # (one trap takes 3 squares in matrix)
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



def handle_event(i_change=0,j_change=0):
    # functions is called whenever player presses keys on keyboard
    # parameters are the changes that are wanted to be
    # applied to player's current location
    list_o_tuples = Soldier.calc_body_indexes(player.get_i_leftcorner() + i_change,
                                              player.get_j_leftcorner()+j_change)

    if Soldier.tuples_in_borders(list_o_tuples):
        player.set_i_leftcorner(player.get_i_leftcorner() + i_change)
        player.set_j_leftcorner(player.get_j_leftcorner()+j_change)
        normal_screen(player)


def memoryad_to_object(hex_ad):
    return ctypes.cast(hex_ad, ctypes.py_object).value

def handle_digit_duration_key(key_pressed,duration_inseconds):
    def substring_after(s, delim):
        return s.partition(delim)[2]

    global player
    global helpful_grid_grass
    global grid_object

    if duration_inseconds <= 1:
       DateBase.update_index(int(key_pressed),player,helpful_grid_grass,grid_object)
    elif duration_inseconds > 1:

         key_pressed=int(key_pressed)
         hex_object_adress=substring_after(DateBase.read_to_display(key_pressed)[0],"at ")
         if "empty" not in DateBase.read_to_display(key_pressed):
            player = memoryad_to_object(hex_object_adress)
            hex_object_adres1 = substring_after(DateBase.read_to_display(key_pressed)[1], "at ")
            helpful_grid_grass = memoryad_to_object(hex_object_adres1)
            hex_object_adres2 = substring_after(DateBase.read_to_display(key_pressed)[2], "at ")
            grid_object = memoryad_to_object(hex_object_adres2)

# ------------------main screen event handling------------------
grid_object=GridMatrix()
grid_object.insert_random_traps()
grid_matrix= grid_object.get_matrix()

helpful_grid_grass=GridMatrix()
helpful_grid_grass.scatter_grass_parallel_matrix()

player=Player()
normal_screen(player)
display_soldair(player)
running = True

# this loop is active as long as player didnt win / lose , or exited the screen
while running:
    if player.check_touch_flag(grid_matrix):
        won_lost_text("You Won!")
        sleep(3 - time() % 3)
        running = False

    # player Lost---> running=False
    if player.check_touch_trap(grid_object):
        won_lost_text("You Lost!")
        sleep(3 - time() % 3)
        running = False

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            t = time() #the time at that moment when line is executed
            digit_pressed = False
            while not keyboard.read_event().event_type == "up" and event.unicode.isdigit():
                digit_pressed = True


            if digit_pressed is True:
                handle_digit_duration_key(event.unicode,(time()-t))
                normal_screen(player)


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


