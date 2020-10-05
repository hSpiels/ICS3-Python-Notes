#Define size of the window
WIDTH = 300
HEIGHT = 300


#Create the first button
button1Draw = [0, 0, 100, 20] #[left, top, width, size]
button1Rect = Rect(button1Draw) #create a rect https://www.pygame.org/docs/ref/rect.html
button1Value = False  #Give the button a vale
button1Color = 'blue' #Give the buttton a color, can also use (r, g, b) sets
#button1Rect.center = (150, 150) #Set the location of the button, discuss rect location values



def on_mouse_up(pos, button): #https://pygame-zero.readthedocs.io/en/stable/hooks.html
    '''Pygame Special Event Hook - Runs when the mouse button is released'''

    global button1Color
    
    #Check to see if button1 is clicked     
    if button1Rect.collidepoint(pos):  #https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint
        print("Button 1 Clicked!")
        
        #Swap color
        if button1Color == 'blue':
            button1Color = 'white'
        else:
            button1Color = 'blue'

  

def draw():

    #Draw the button on the screen
    screen.draw.filled_rect(button1Rect, button1Color) #filled_rect(rect, (r, g, b)) #could just use rect    