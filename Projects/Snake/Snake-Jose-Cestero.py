from pickle import TRUE
import time
import pygame
import random
pygame.init()


red = (205,92,92) #for when game is over
snake = (173,216,230) #snake color
black = (41,36,33) #score color
white = (255,255,255) #background
dis_width = 800
dis_height = 600

dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("SNAKE GAME JOSE C")
game_over = False

snake_block = 20
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)

def myScore(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def playerSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake, [x[0], x[1], snake_block, snake_block])

def mssg(message, color):
    messages = font_style.render(message, True, color)
    dis.blit(messages, [(dis_width)/3.5, (dis_height)/2])

def gameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = (dis_height)/2

    x1_change = 0
    y1_change = 0

    snake_List = []
    snakes_length = 1

    foodsx = round(random.randrange(0, dis_width - snake_block) / 20) *20
    foodsy = round(random.randrange(0, dis_width - snake_block) / 20) *20

    while not game_over:
        while game_close == True:
            dis.fill(white)
            mssg("You sadly lost :(, press R to retry or E to exit the game!", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameRestart()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, red, [foodsx, foodsy, snake_block, snake_block]) #make apple or whatever the food is supposed to be
        myScore(snakes_length-1)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snakes_length:
            del snake_List[0]

        for x in snake_List[-1]:
            if x == snake_Head:
                game_close = True

        playerSnake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodsx and y1 == foodsy:
            foodsx = round(random.randrange(0, dis_width - snake_block)/20) * 20
            foodsy = round(random.randrange(0, dis_height - snake_block)/20) * 20
            snakes_length += 1


        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameRestart()

