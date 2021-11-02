import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    

    # Set up some data to describe a small circle and its color
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE = pygame.Color(0,0,255)
    
    circleColor = RED        # A color is a mix of (Red, Green, Blue)
    circlePos = [50,50]
    moveCircleRight = False #Control whether the circle should move or not

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                moveCircleRight = True
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_RIGHT:
                moveCircleRight = False
            
  

        # Update your game objects and data structures here...
        if moveCircleRight:
            circlePos[0] += 0.05

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

               
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, circlePos, 20)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()

