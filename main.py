import pygame
import random

pygame.init()

display_width = 400
display_height = 400
white = (255,255,255)
black = (0,0,0)
light_grey = (165,175,185)
light_red = (255,0,0)
red = (200,0,0)
green = (34,177,76)
light_green = (0,255,0)
blue = (0,128,255)

smallfont = pygame.font.SysFont(None,25)
midfont = pygame.font.SysFont(None,50)
largefont = pygame.font.SysFont(None,75)

img = pygame.image.load('img/one.png')
img1 = pygame.image.load('img/two.png')
img2 = pygame.image.load('img/three.png')
img3 = pygame.image.load('img/four.png')
img4 = pygame.image.load('img/five.png')
img5 = pygame.image.load('img/six.png')
dices = [img,img1,img2,img3,img4,img5]

gameDisplay = pygame.display.set_mode((display_width,display_height))

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = midfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()


def text_to_button(msg,color,buttonx,buttony,buttonw,buttonh,size = "small"):
    textSurf, textRect = text_objects(msg,color,"small")
    textRect.center = ((buttonx+(buttonw/2)), buttony+(buttonh/2))
    gameDisplay.blit(textSurf,textRect)


def button(text, x, y, width, height, inactive_color, active_color, params, action = None,):
    cur = pygame.mouse.get_pos()
    #print(cur)
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "play":
                roll(params)
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
    
    text_to_button(text,black,x,y,width,height)


def roll(number_dice):
    dice = random.choice(dices)
    dice1 = random.choice(dices)
    dice2 = random.choice(dices)
    if number_dice == "1":
        print("1 Dice")
        gameDisplay.fill(white)
        bird_rect = dice.get_rect(center=(200,200))
        gameDisplay.blit(dice,bird_rect)
    elif number_dice == "2":
        print("2 Dice")
        gameDisplay.fill(white)
        bird_rect = dice.get_rect(center=(130,200))
        bird_rect1 = dice1.get_rect(center=(250,200))
        gameDisplay.blit(dice,bird_rect)
        gameDisplay.blit(dice1,bird_rect1)
    elif number_dice == "3":
        print("3 Dice")
        gameDisplay.fill(white)
        bird_rect = dice.get_rect(center=(80,200))
        bird_rect1 = dice1.get_rect(center=(200,200))
        bird_rect2 = dice2.get_rect(center=(320,200))
        gameDisplay.blit(dice,bird_rect)
        gameDisplay.blit(dice1,bird_rect1)
        gameDisplay.blit(dice2,bird_rect2)
    else:
        print("Invalid value!")


def gameLoop():
    pygame.display.set_caption('Dice Rolling Simulator')
    gameDisplay.fill(white)
    number_dice = ''
    input_rect = pygame.Rect(175,75,50,30)
    
    while True:
        
        for event in pygame.event.get():
            print(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    number_dice = number_dice[0:-1]
                    
                    gameDisplay.fill(white)
                elif len(number_dice) < 1:
                    number_dice += event.unicode
                    print(number_dice)
                    roll(number_dice)

                elif event.key == pygame.K_RETURN:
                    number_dice = number_dice

        
        
        text_to_button("Number of Dice: ",black,75,75,50,30)
        text_to_button("(max 3) ",black,75,90,50,30)

        
        text_surface = smallfont.render(number_dice,True,black)
        gameDisplay.blit(text_surface,(input_rect.x+10,input_rect.y+5))
        pygame.draw.rect(gameDisplay, blue,input_rect,3)


        button("Roll",50,300,100,50, green, light_green,number_dice,action="play")
        button("Quit",250,300,100,50, red, light_red,None,action="quit")


        pygame.display.update()



if __name__ == '__main__':
    gameLoop()
    
    
    
    
    
    
