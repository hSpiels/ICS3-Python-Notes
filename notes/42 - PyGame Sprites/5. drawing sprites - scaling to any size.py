import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    spriteSheet = pygame.image.load("images/dungeon/0x72_DungeonTilesetII_v1.3.png")
    #spriteSheet = pygame.transform.scale2x(spriteSheet)
    scale = 0.5;
    spriteSheet = pygame.transform.smoothscale(spriteSheet, (scale*spriteSheet.get_width(),scale*spriteSheet.get_height()))
    
    wizardPos = [0,50]
    lizardPos = [0,150]
    
    #These are needed for the image animation
    lizardRect = [128*scale,236*scale,16*scale,28*scale]  #Old Values
    #lizardRect = [256,472,32,56]  #New values are doubled since I doubled the scale
    lizardPatchNumber = 0         #Start at the initial patch
    lizardNumPatches = 4          #Only use 4 patches
    lizardFrameCount = 0          #Start at intial frame
    
    lizardFrameRate = 10;
    
    
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        #Move the Dino
        wizardPos[0] += 0.5   #update the x for the lizard
        lizardPos[0] += 0.5   #update the x for the wizard
        
        if (frameCount % lizardFrameRate == 0):    #Only change the animation frame once every {lizardFrameRate} frames
            if (lizardPatchNumber < lizardNumPatches-1) :
                lizardPatchNumber += 1
                lizardRect[0] += lizardRect[2]  #Shift the "display window" to the right along the sprite sheet by the width of the image
            else:
                lizardPatchNumber = 0           #Reset back to first patch
                lizardRect[0] -= lizardRect[2]*(lizardNumPatches-1)  #Reset the rect position of the rect back too
                #self.imageRect = copy.copy(self.origImageRect)
            
            print(f"Patch Number: {lizardPatchNumber}   Image Rect: {lizardRect}  ")
            
        #Draw the image of the sprite using the rect
        mainSurface.blit(spriteSheet, wizardPos, [130,165,16,28])  #Positions found using msPaint
        mainSurface.blit(spriteSheet, lizardPos, lizardRect)  #Positions found using msPaint
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        frameCount += 1;
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
