import pygame
import random
import math

class Ball():
    
    def __init__(self, posIn, sizeIn, colorIn):
        self.pos = posIn
        self.size = sizeIn
        self.color = colorIn
        self.fallSpeed = 0 #Define the falling speed of the circle
        self.gravity = 1
        
    def draw(self, surfaceIn):
        pygame.draw.circle(surfaceIn, self.color, self.pos, self.size)
    
    def update(self):
        #Make the circle fall if needed by adjusting it's y value
        self.pos[1] += self.fallSpeed
        self.fallSpeed += self.gravity
    
    def jump(self):
        self.fallSpeed = -20
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
        
    def setPos(self, posIn):
        self.pos = posIn
   
    

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the ball object using it's position, size and color
    circlePos = [250,30]
    circle = Ball(circlePos, 30, (255, 0, 0))        # A color is a mix of (Red, Green, Blue)
      
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if ev.type == pygame.MOUSEBUTTONUP:
            #Make the circle jump
            print("jump!")
            circle.jump()
            pass
            
        # Update your game objects and data structures here...
        circle.update()
                
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        #Draw the circle on the screen
        circle.draw(mainSurface)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
