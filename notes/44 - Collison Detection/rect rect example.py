#-----------------------------------------------------------------------------
# Name:        Rect Rect Collision Example
# Purpose:     To demonstrate how rect-rect collision works
#
# Author:      Ms. Bokhari, Mr. Brooks
# Created:     21-Feb-2021
# Updated:     21-Sept-2021

#TODO: Need to properly comment this example
#-----------------------------------------------------------------------------

from pygame import *

init()

RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LBLUE = (21,244,238)
BORANGE = (255,173,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
info = display.Info()
width = 700
height = 500

SIZE = (width, height)
screen = display.set_mode(SIZE)#,FULLSCREEN)

#some game states
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False

STATECGREEN = 0
STATECBLUE = 1
STATECLEAR = 3

def displayState(screen,state):
  if state == STATECGREEN:
    stringCG= "Green-Red Collision"
    text = myFont.render(stringCG, 1, YELLOW)
    screen.blit(text, (width - 400, 50,100,100))

  if state == STATECBLUE:
    stringCB= "Blue-Red Collision"
    text = myFont.render(stringCB, 1, PURPLE)
    screen.blit(text, (width - 400, 50,100,100))

  if state == STATECLEAR:
    stringC= "                                              "
    text = myFont.render(stringC, 1,BLACK)
    screen.blit(text, (width - 400, 50,100,100))
  

def displayCo(screen,box,clr):
  (xl,yl) = box.topleft
  stringtl= "("+ str(xl)+"," +str(yl)+ ")"
  (xr,yr) = box.topright
  stringtr= "("+ str(xr)+"," +str(yr)+ ")"
  (xbr,ybr) = box.bottomright
  stringbr= "("+ str(xbr)+"," +str(ybr)+ ")"
  (xb,yb) = box.bottomleft
  stringbl= "("+ str(xb)+"," +str(yb)+ ")"
  text1 = myFont.render(stringtl, 1, clr)
  text2 = myFont.render(stringtr, 1, clr)
  text3 = myFont.render(stringbr, 1, clr)
  text4 = myFont.render(stringbl, 1, clr)
  screen.blit(text1, Rect(xl-35,yl-20, 20, 20))
  screen.blit(text2, Rect(xr-15,yr-20, 20, 20))
  screen.blit(text3, Rect(xbr-15,ybr+5, 20, 20))
  screen.blit(text4, Rect(xb-35,yb+5, 20, 20))

def checkForCollision(rect1, rect2):
  if rect1.colliderect(rect2):
    return True
  return False

def drawScreen(screen,red,green,blue,state):
 
  draw.rect(screen, BLACK, (0, 0, width, height))
  draw.rect(screen,GREEN, green)
  draw.rect(screen,BLUE, blue)
  draw.rect(screen, RED,red)
  string= "Move the red box with the arrow keys"
  text = myFont.render(string, 1, WHITE)
  screen.blit(text, (width - 400, 20,100,100))
  displayCo(screen,red,WHITE)
  displayCo(screen,green,GREEN)
  displayCo(screen, blue,LBLUE)
  displayState(screen,state)

  display.flip()

myClock = time.Clock()
running = True
x = width//2
y= height//2
mx=my=0
greenRect = Rect(50,50,100,100)
redRect = Rect(x,y,100,100)
blueRect = Rect(400,400,50,50)
myFont = font.SysFont("Times New Roman",18)
while running:
  for evnt in event.get():
    if evnt.type == QUIT:
      running = False
    #key is pressed
    if evnt.type == KEYDOWN:
      if evnt.key == K_LEFT:
        KEY_LEFT = True
      if evnt.key == K_RIGHT:
        KEY_RIGHT = True
      if evnt.key == K_UP:
        KEY_UP = True
      if evnt.key == K_DOWN:
        KEY_DOWN = True
    #key is released 
    if evnt.type == KEYUP:
      if evnt.key == K_LEFT:
        KEY_LEFT = False
      if evnt.key == K_RIGHT:
        KEY_RIGHT = False
      if evnt.key == K_UP:
        KEY_UP = False
      if evnt.key == K_DOWN:
        KEY_DOWN = False
    if evnt.type == MOUSEBUTTONDOWN:
        mx, my = evnt.pos          
        button = evnt.button
    if evnt.type == MOUSEMOTION:
        mx, my = evnt.pos


  if KEY_LEFT == True:
    redRect[0] -= 1
  if KEY_RIGHT == True:
    redRect[0] += 1
  if KEY_UP == True:
    redRect[1] -= 1
  if KEY_DOWN == True:
    redRect[1] += 1

  if checkForCollision(redRect, greenRect) == True:
    state = STATECGREEN

  elif checkForCollision(redRect, blueRect) == True:
    state = STATECBLUE

  else:
    state = STATECLEAR
  drawScreen(screen,redRect,greenRect,blueRect,state)
  display.flip()
  myClock.tick(60)

quit()