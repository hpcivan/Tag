
import pygame
import sys
import random

def player_movement(keys):
    #Receives a list of all key movements
    #Player 1
    vel = 3
    if keys[pygame.K_LEFT]:
        player1_rect.x -= vel
    if keys[pygame.K_RIGHT]:
        player1_rect.x += vel
    if keys[pygame.K_UP]:
        player1_rect.y -= vel
    if keys[pygame.K_DOWN]:
        player1_rect.y += vel
    #Player 2
    if keys[pygame.K_w]: #up
        player2_rect.y -= vel
    if keys[pygame.K_s]: #down
        player2_rect.y += vel
    if keys[pygame.K_a]: #left
        player2_rect.x -= vel
    if keys[pygame.K_d]: #right
        player2_rect.x += vel

def player_collision(player_choice):
    if player1_rect.colliderect(player2_rect):
        #Code to change the text - can only be Player 1 or Player 2
        if player_choice == 1:
            player_choice = 2
        else:
            player_choice = 1

        #Resets position after a tag
        player1_rect.x = 10
        player2_rect.x = 300
    return player_choice

def wall_collision():
    #Could be a better way to do this?
    #Checks for wall collision - doesn't allow rects to go past
    if player1_rect.right >= screen_width:
        player1_rect.right = screen_width
    if player2_rect.right >= screen_width:
        player2_rect.right = screen_width
    if player1_rect.left <= 0:
        player1_rect.left = 0
    if player2_rect.left <= 0:
        player2_rect.left = 0
    if player1_rect.top <= 0:
        player1_rect.top = 0
    if player2_rect.top <= 0:
        player2_rect.top = 0
    if player1_rect.bottom >= screen_height:
        player1_rect.bottom = screen_height
    if player2_rect.bottom >= screen_height:
        player2_rect.bottom = screen_height

pygame.font.init()
base_font = pygame.font.Font(None,32)

player_list = [1,2]
player_choice = random.choice(player_list)  # set random player at beginning of game

pygame.init()

#setting up game variables
screen_width, screen_height = 600, 600

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

player1_rect = pygame.Rect(500,30,40,40)
player2_rect = pygame.Rect(5,30,40,40)

#unused code at this stage
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    # for continuous movement, rather than single keypress
    #note this isn't handled in the event loop
    keys = pygame.key.get_pressed()
    player_movement(keys)

    #screen drawing
    screen.fill((175,215,70))
    pygame.draw.rect(screen, pygame.Color('red'), player1_rect)
    pygame.draw.rect(screen, pygame.Color('blue'), player2_rect)

    #Text rendering
    player_choice = player_collision(player_choice) #two-in-one function - updates text and checks for collision
    text = "Player {} is it".format(str(player_choice))
    text_surface = base_font.render(text, True,(255,255,255))
    screen.blit(text_surface, (screen_width/2-60,30))



    wall_collision()

    pygame.display.update()
    clock.tick(60)