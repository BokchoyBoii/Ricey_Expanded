# -*- coding: cp1252 -*-
import pygame
import time
import random
pygame.init()
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
car_width=70
car_height = 154
UI =(149, 165, 166)
emerald =(39, 174, 96)
pomegranate =(192, 57, 43)
pom =(231, 76, 60)
em =(46, 204, 113)
grade = {0:"F-",1:"F", 2:"F+",3:"D-",4:"D",5:"D+",6:"C-",7:"C",8:"C+",9:"B-",10:"B",11:"B+",12:"A-",13:"A",14:"A+"}
crash_sound = pygame.mixer.Sound("crashsound.wav")
pygame.mixer.music.load('music.wav')

icon = pygame.image.load('icon.png')

pygame.display.set_icon(icon)

score = 0
creditsIMG = pygame.image.load('credits.png')
pygame.display.set_caption('Ricey')

clock = pygame.time.Clock()
thingIMG = pygame.image.load('thing.png')
gameover= pygame.image.load('gameover.png')
charImg = pygame.image.load('Char.png')
backgroundIMG = pygame.image.load('background.png')
victoryIMG = pygame.image.load('victory.png')
extracreditIMG = pygame.image.load('extracredit.png')
victory2IMG = pygame.image.load('victory2.png')













def credits_():
    
    gameDisplay.blit(creditsIMG,(0,0))
    pygame.display.update()
    time.sleep(10)
    
    
    pygame.QUIT()





def crash2():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    


    gameDisplay.blit(gameover,(0,0))

    

    pygame.display.update()
    time.sleep(3)
    game_loop2()






def things2(thingx,thingy):
    
    gameDisplay.blit(extracreditIMG,(thingx,thingy))





def endplate(score):
    font = pygame.font.Font("freesansbold.ttf", 70)
    text = font.render("Grade : "+ grade[score], True, red)
    gameDisplay.blit(text,(250,400))
            
    pygame.display.update



def victory2():
    gameDisplay.blit(victory2IMG,(0,0))
    pygame.display.update()
    time.sleep(2)
    credits_()
def things_dodged(score):
    
    font = pygame.font.Font("freesansbold.ttf", 36)
    text = font.render("Grade : "+ grade[score], True, black)
    gameDisplay.blit(text,(0,0))


def things(thingx, thingy,):
    gameDisplay.blit(thingIMG,(thingx,thingy))

def char(x,y):
    gameDisplay.blit(charImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font("freesansbold.ttf",80)
    TextSurf, TextRect=text_objects(text, largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()

    
def victory():

    gameDisplay.blit(victoryIMG,(0,0))
    pygame.display.update()
    time.sleep(2)
    game_loop2()
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    



    gameDisplay.blit(gameover,(0,0))

    

    pygame.display.update()
    time.sleep(3)
    game_loop()

   







    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(UI)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Ricey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start",150,450,100,50,emerald,em,game_loop)
        button("Quit :'(",550,450,100,50,pomegranate,pom,quitgame)

        pygame.display.update()
        clock.tick(15)



def game_loop():
    x = (display_width * 0.45)
    score = 0
    y = (display_height * 0.75)
    pygame.mixer.music.play(-1)
    x_change = 0
    thing_width = 100
    limit_x = (display_width - thing_width)
    thing_startx = random.randrange(0, limit_x)
    thing_starty = -600
    thing_speed = 9
    thing_width = 100
    thing_height = 100
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -8
                if event.key == pygame.K_d:
                    x_change = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change
                    
        things_dodged(score)
        
        gameDisplay.fill(white)
        gameDisplay.blit(backgroundIMG,(0,0))

        
        things(thing_startx, thing_starty)
        thing_starty += thing_speed

        

        char(x,y)

        if x > display_width- car_width or x < 0:
            endplate(score)
            crash()
           
        if score == 14:
            
            victory()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,limit_x)
            score += 1
            thing_speed += 1
            
            things_dodged(score)

        ####
        if y < thing_starty+thing_height:
            print ""
            
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                endplate(score)
                crash()
                

               

        ####
        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render("Level 1", True, black)
        gameDisplay.blit(text,(670,0))


        things_dodged(score)

        pygame.display.update()
        clock.tick(60)
def game_loop2():
    x = 0
    score = 0
    y = (display_height * 0.75)
    pygame.mixer.music.play(-1)
    x_change = 0
    y_change = 0
    gameExit = False
    thing_width = 300
    limit_x = (display_width - thing_width)

    
    thing_startx = random.randrange(0, limit_x)
    thing_starty = -600
    thing_speed = 7
    thing_height = 100




    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -8
                if event.key == pygame.K_d:
                    x_change = 8
                if event.key == pygame.K_w:
                    y_change = -8
                if event.key == pygame.K_s:
                    y_change = 8
                    
                    




                    

            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

        
        
        
        x += x_change
        y += y_change         
        



        
        

        

        gameDisplay.fill(white)
        gameDisplay.blit(backgroundIMG,(0,0))
        things_dodged(score)
        font = pygame.font.Font("freesansbold.ttf", 25)
        text = font.render("Get extra credit!", True, emerald)
        gameDisplay.blit(text,(360,0))
        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render("Level 2", True, black)
        gameDisplay.blit(text,(670,0))
        things2(thing_startx, thing_starty)
        thing_starty += thing_speed
        

        char(x,y)

        if x > display_width- car_width or x < 0:
            endplate(score)
            crash2()
           
        if score == 14:
            
            victory2()

        

        ####
        if y < thing_starty+thing_height:
        
            
 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, limit_x)
                score += 1
                thing_speed += 1
                
            
                things_dodged(score)
            else:
                endplate(score)
                crash2()
        ####
        

        pygame.display.update()
        clock.tick(60)



print " _____  _                 "
print "|  __ \(_)                "
print "| |__) |_  ___ ___ _   _  "
print "|  _  /| |/ __/ _ \ | | | "
print "| | \ \| | (_|  __/ |_| | "
print "|_|  \_\_|\___\___|\__, | "
print "                    __/ | "
print "                   |___/  "
print "                          "
print "                          "
print "                          "
print "    ©2015 Dumhed Ltd.     "
print "                          "
print "                          "
print "        Controls          "
print "        A - Left          "
print "        D - Right         "    

game_intro()
game_loop()
pygame.QUIT()
quit()
