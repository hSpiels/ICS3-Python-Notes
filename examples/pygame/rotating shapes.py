import pygame
import math

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 400   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower


    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    # Set up some data to describe a small circle and its color
    circleColor = (134, 20, 227)        # A color is a mix of (Red, Green, Blue)
    angle = 0;

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        #Drawing a Rect without rotation
        pygame.draw.rect(mainSurface,(255,0,0), [10,10,20,100])
        
        #Drawing a Rotated Rect.
        rectSurface = pygame.Surface( (100,100) ) #Make the new surface
        rectSurface.fill((255,0,255,0));          #Fill with a background color
        #rectSurface.set_colorkey((255,0,255))     #Set the background color to be transparent
                
        pygame.draw.rect(rectSurface,(0,255,0), [10,10,20,100]) #Draw a rect on the surface
        angle += 1
        print(angle)
        rectSurface = pygame.transform.rotate(rectSurface,angle)   #Rotate the surface and redraw
        
        #Draw an Arc
        pygame.draw.arc(mainSurface, (255,0,0), (200,200,200,50),0,math.radians(362))
        
        
        
        pygame.Surface.blit(mainSurface,rectSurface, (0,0));    #Draw the rectSurface onto the mainSurface
        
        
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()