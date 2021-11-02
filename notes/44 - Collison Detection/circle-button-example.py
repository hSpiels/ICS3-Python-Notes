import pygame
import random
import math

def distFromPoints(point1, point2):
    '''
    This function calculationes the distance between two points given by a set of tuples (x1,y1) and (x2,y2)
    
    Parameters
    ----------
    point1 : float
        The first point to compare
    point2 : float
        The second point to compare
        
    Returns
    float
        The distance between the two points
    '''
    distance = math.sqrt( ((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2) )
    
    return distance
  

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Create the the size, position and color for a circle
    circlePos  = [200,200] #[x,y]
    circleSize = 30
    circleColor = (255,0,0)
    
    #Create a variable to save the button state
    buttonOn = False
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if ev.type == pygame.MOUSEBUTTONUP:
            if distFromPoints(circlePos,mouseCirclePos) < (circleSize):
                buttonOn = not buttonOn
                
                
        # Update your game objects and data structures here...
        mouseCirclePos = pygame.mouse.get_pos()
            
        if buttonOn:
            circleColor = (100,0,0)
        else:
            circleColor = (255,0,0)
        
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize) #Draw Circle      

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
