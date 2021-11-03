import pygame
  
def main():
    #-----------------------------Setup------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))

    #-----------------------------Program Variable Initialization----------------------#

    # Create the the size, position and color for a circle
    circlePosX  = 200
    circlePosY = 200
    circleSize = 30
    circleColor = (255,0,0)
    circleSpeedY = 0;
    jumping = False
    
    groundLevel = 400
    
    

   #-----------------------------Main Game Loop----------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if ev.type == pygame.MOUSEBUTTONUP:
            #You can only jump if you are not already jumping
            if (not jumping):
                #Going up
                circleSpeedY = -20
                
                #Disallow jumping since already in the air
                jumping = True
 
        #-----------------------------Game Logic---------------------------------------#
       
        #Move the circle
        circlePosY += circleSpeedY
        
        #Is the player colliding with the ground?
        if ((circlePosY + circleSize) > groundLevel):
            #Snap the player's bottom to the ground
            circlePosY = groundLevel - circleSize
            
            #Stop the circle falling
            circleSpeedY = 0
            
            #Allow jumping
            jumping = False
        
        #The circle is not colliding with the ground
        else:
            #Gravity acclerates the movement speed
            circleSpeedY += 1
        
        #-----------------------------Drawing Everything-------------------------------#
        # So fill everything with the background color
        mainSurface.fill((0, 200, 255))
      
        #Draw the ground
        pygame.draw.rect(mainSurface,(200,200,200), (0,groundLevel,surfaceSize,surfaceSize-groundLevel))
        #Draw the Circle
        pygame.draw.circle(mainSurface, circleColor, (circlePosX,circlePosY), circleSize)         
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
