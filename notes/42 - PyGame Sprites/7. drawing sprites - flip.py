#TODO: Update this example showing how to use a temporary surface and pygame.transform.flip(tempSurface,True,False)
import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    #----------------------Set up the game------------#  

    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    spriteSheet = pygame.image.load("images/dungeon/0x72_DungeonTilesetII_v1.3.png")
    spriteSheet = pygame.transform.scale2x(spriteSheet)
    
    wizardPos = [0,50]
    lizardPos = [0,150]
    
    #These are needed for the image animation
    lizardRect = [176,236,16,28]  #Old Values
    lizardRect = [352,472,32,56]  #New values are doubled since I doubled the scale
    lizardPatchNumber = 0         #Start at the initial patch
    lizardNumPatches = 5          #Only use 4 patches
    lizardFrameCount = 0          #Start at intial frame
    lizardFrameRate = 10;         #How often to re-draw the lizard
    lizardDirection = 'Right'     #Control which direction lizard is facing
    lizardSpeed = 0.5
    
    lizardMove = True            #Control whether the lizard can move
    
    while True:
        
        #----------------------Check all the events to see if anything is happening------------#  

        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            lizardMove = True
        elif ev.type == pygame.MOUSEBUTTONUP:
            lizardMove = False
        elif ev.type == pygame.KEYUP:          #Add some key handling to make space change lizard's direction
            if ev.key == pygame.K_SPACE:
                if lizardDirection == 'Right':
                    lizardDirection = 'Left'
                else:
                    lizardDirection = 'Right'



 

        #----------------------Game Logic Goes After Here----------------------------#  
        # Update your game objects and data structures here...

        #Game logic for the lizard
        if (lizardMove):  #Check if the lizard should move
            #Move the Dino
            if lizardDirection =='Right': #Lizard goes right
                lizardPos[0] += lizardSpeed     #update the x for the lizard
            else:                               #Lizard goes left
                lizardPos[0] -= lizardSpeed     #update the x for the lizard
            
            if (frameCount % lizardFrameRate == 0):    #Only change the animation frame once every {lizardFrameRate} frames
                if (lizardPatchNumber < lizardNumPatches-1) :
                    lizardPatchNumber += 1
                    lizardRect[0] += lizardRect[2]  #Shift the "display window" to the right along the sprite sheet by the width of the image
                else:
                    lizardPatchNumber = 0           #Reset back to first patch
                    lizardRect[0] -= lizardRect[2]*(lizardNumPatches-1)  #Reset the rect position of the rect back too
                    #self.imageRect = copy.copy(self.origImageRect)
                
                print(f"Patch Number: {lizardPatchNumber}   Image Rect: {lizardRect}  ")
          
          
          
        #Game Logic for the wizard
        wizardPos[0] += 0.5   #update the x for the wizard
        
        
        
        #----------------------Draw all the images----------------------------#  
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))
        
        #Draw the image of the wizard sprite using the rect
        mainSurface.blit(spriteSheet, wizardPos, [130,165,16,28])  #Positions found using msPaint
        
        
        #Draw the image of the lizard sprite using the rect
        #mainSurface.blit(spriteSheet, lizardPos, lizardRect)  #Positions found using msPaint
        tempSurface = pygame.Surface( (lizardRect[2], lizardRect[3]) ) #Make a temp Surface using the width and height of the rect
        tempSurface.fill((1,1,1))
        tempSurface.set_colorkey((1,1,1))                                      #Set the color black to be transparent
        tempSurface.blit(spriteSheet, (0,0),  lizardRect)                      #Copy the lizard image to the temp surface
        
        if lizardDirection == 'Left':
            tempSurface = pygame.transform.flip(tempSurface,True,False)
        
        mainSurface.blit(tempSurface, lizardPos)  #Positions found using msPaint
        
        
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        #----------------------Set your frame rate----------------------------#  

        frameCount += 1;
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
