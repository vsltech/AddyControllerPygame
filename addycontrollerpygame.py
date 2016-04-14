import random, pygame, sys
from pygame.locals import *
#import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#WHEELS
Motor1A = 15
Motor1B = 13
Motor1E = 11
 
Motor2A = 36
Motor2B = 38
Motor2E = 40
#ARM
ARM1A = 19
ARM1B = 21
ARM1E = 23
 
ARM2A = 16
ARM2B = 18
ARM2E = 22
#LED
LED = 37

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(ARM1A,GPIO.OUT) 
GPIO.setup(ARM1B,GPIO.OUT) 
GPIO.setup(ARM1E,GPIO.OUT) 
GPIO.setup(ARM2A,GPIO.OUT) 
GPIO.setup(ARM2B,GPIO.OUT) 
GPIO.setup(ARM2E,GPIO.OUT) 

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(ARM1E,GPIO.LOW)
GPIO.output(ARM2E,GPIO.LOW)

def ledon():
    print "LED ON"
    os.system('mpg123 -q on.mp3 &')
    GPIO.output(LED,GPIO.HIGH)
    
def ledoff():
    print "LED OFF"
    os.system('mpg123 -q off.mp3 &')
    GPIO.output(LED,GPIO.LOW)
    
def armforward():
    print "ARM forwards"
    os.system('mpg123 -q movingarm.mp3 &')
    GPIO.output(ARM1A,GPIO.HIGH)
    GPIO.output(ARM1B,GPIO.LOW)
    GPIO.output(ARM1E,GPIO.HIGH)
    
def armbackward():
    print "ARM backwards"
    os.system('mpg123 -q movingarm.mp3 &')
    GPIO.output(ARM1A,GPIO.LOW)
    GPIO.output(ARM1B,GPIO.HIGH)
    GPIO.output(ARM1E,GPIO.HIGH)
    
def armstop():
    GPIO.output(ARM1E,GPIO.LOW)
    os.system('mpg123 -q stop.mp3 &')

def griploose():
    print "GRIP loosing"
    os.system('mpg123 -q movinggrip.mp3 &')
    GPIO.output(ARM2A,GPIO.HIGH)
    GPIO.output(ARM2B,GPIO.LOW)
    GPIO.output(ARM2E,GPIO.HIGH)

def griptight():
    print "GRIP tightining"
    os.system('mpg123 -q movinggrip.mp3 &')
    GPIO.output(ARM2A,GPIO.LOW)
    GPIO.output(ARM2B,GPIO.HIGH)
    GPIO.output(ARM2E,GPIO.HIGH)

def gripstop():
    GPIO.output(ARM2E,GPIO.LOW)
    os.system('mpg123 -q stop.mp3 &')

def forward():
    print "Going forwards"
    os.system('mpg123 -q movingforward.mp3 &')
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def right():
    print "Going right"
    os.system('mpg123 -q turningright.mp3 &')
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
                
    GPIO.output(Motor2E,GPIO.LOW)
    
def left():
    print "Going left"
    os.system('mpg123 -q turningleft.mp3 &')
    GPIO.output(Motor1E,GPIO.LOW)
                
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

def backward():
    print "Going backward"
    os.system('mpg123 -q movingbackward.mp3 &')
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def clean():
    GPIO.cleanup()
    
def stop():
    print "Now stop"
    #os.system('mpg123 -q stop.mp3 &')
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

##########################################################
FPS = 15
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('ADDY Controller')
    os.system('mpg123 -q pleasewaitstarting.mp3 &')
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
     DISPLAYSURF.fill(BGCOLOR)
     bg = pygame.image.load("addyver2.jpg").convert()
     DISPLAYSURF.blit(bg, (0, 0))   
     pygame.display.update()

     while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_a):
                    left()
                elif (event.key == K_d):
                    right()
                elif (event.key == K_w):
                   
                    forward()
                elif (event.key == K_UP):
                    armforward()
                elif (event.key == K_s):
                   
                    backward()
                elif (event.key == K_DOWN):
                    armbackward()
                elif (event.key == K_LEFT):
                  
                    griploose()
                elif (event.key == K_RIGHT):
                   
                    griptight()
                elif (event.key == K_h):
                  
                    os.system('mpg123 -q horn.mp3 &')
                elif (event.key == K_l):
                  
                    ledon()
                elif (event.key == K_o):
                    
                    ledoff()
                elif event.key == K_SPACE:
                 
                    os.system('mpg123 -q stop.mp3 &')
                    stop()
                elif event.key == K_ESCAPE:
                    
                    os.system('mpg123 -q stop.mp3 &')
                    stop()
                    terminate()
            elif event.type == KEYUP:
                DISPLAYSURF.fill(WHITE)
                pygame.display.update()
                stop()
                gripstop()
                armstop()

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to start', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)



# KRT 14/06/2012 rewrite event detection to deal with mouse use
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:      #event is quit 
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:   #event is escape key
                terminate()
            else:
                return event.key   #key found return with it
    # no quit or key events in queue so return None    
    return None

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('CONTROLLER', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('ADDY', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    
#KRT 14/06/2012 rewrite event detection to deal with mouse use
    pygame.event.get()  #clear out event queue
    
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()
#KRT 14/06/2012 rewrite event detection to deal with mouse use
        if checkForKeyPress():
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
