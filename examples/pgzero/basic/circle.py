brush_location = (0,0)

def on_mouse_move(pos):
    global brush_location
    brush_location = pos

def draw():
    #screen.clear()
    screen.draw.circle(brush_location, 30, 'white')

