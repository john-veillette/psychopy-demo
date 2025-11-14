from psychopy import visual
import numpy as np

GRID_DIM = 7
GRID_SIZE = 3/4. # in fractions of window height

def _get_square_locs(i, j):
    square_width = GRID_SIZE / GRID_DIM
    start = -GRID_SIZE/2 # from center
    x = start + i*square_width + square_width/2
    y = start + j*square_width + square_width/2
    return x, y


def esg(win, mouse):
    '''
    Draws an evaluative space grid and collects a mouse response

    Parameters
    ----------
    win : psychopy.visual.Window object
    mouse : psychopy.event.Mouse

    Returns
    ----------
    positive : int
        Likert score on positive dimension
    negative : int
        Likert score on negative dimension
    '''
    # make grid of squares
    grid = np.empty((GRID_DIM, GRID_DIM), dtype = object)
    for i in range(GRID_DIM):
        for j in range(GRID_DIM):
            grid[i, j] = visual.Rect(
                win, size = GRID_SIZE/GRID_DIM,
                pos = _get_square_locs(i, j),
                fillColor = 'white',
                lineColor = 'black',
                units = 'height' # sizes/locations in fractions of window height
                )
            grid[i, j].draw() # will appear on next screen flip
    xlab = visual.TextStim(
        win, 'More positive →',
        pos = (0, -GRID_SIZE/2 - GRID_SIZE/GRID_DIM/2),
        units = 'height',
        height = GRID_SIZE/GRID_DIM/2
        )
    xlab.draw()
    ylab = visual.TextStim(
        win, 'More negative →',
        pos = (-GRID_SIZE/2 - GRID_SIZE/GRID_DIM/2, 0),
        units = 'height',
        height = GRID_SIZE/GRID_DIM/2,
        ori = 270
        )
    ylab.draw()
    win.flip()

    # keep polling for response until we get one
    while True:
        for i in range(GRID_DIM):
            for j in range(GRID_DIM):
                if mouse.isPressedIn(grid[i, j]):
                    win.flip() # clear screen
                    return i + 1, j + 1 # automatically stops loop



def esg_fancy(win, mouse, square_size = .1):
    '''
    Draws an evaluative space grid and collects a mouse response.
    Keeps redrawing until response collected, such that square
    mouse is hovering over is highlighted in red. 

    Parameters
    ----------
    win : psychopy.visual.Window object
    mouse : psychopy.event.Mouse

    Returns
    ----------
    positive : int
        Likert score on positive dimension
    negative : int
        Likert score on negative dimension
    '''
    # make grid of squares
    grid = np.empty((GRID_DIM, GRID_DIM), dtype = object)
    for i in range(GRID_DIM):
        for j in range(GRID_DIM):
            grid[i, j] = visual.Rect(
                win, size = GRID_SIZE/GRID_DIM,
                pos = _get_square_locs(i, j),
                fillColor = 'white',
                lineColor = 'black',
                units = 'height',
                autoDraw = True # draw on every screen flip until turned off
                )
    xlab = visual.TextStim(
        win, 'More positive →',
        pos = (0, -GRID_SIZE/2 - GRID_SIZE/GRID_DIM/2),
        units = 'height',
        height = GRID_SIZE/GRID_DIM/2
        )
    xlab.autoDraw = True
    ylab = visual.TextStim(
        win, 'More negative →',
        pos = (-GRID_SIZE/2 - GRID_SIZE/GRID_DIM/2, 0),
        units = 'height',
        height = GRID_SIZE/GRID_DIM/2,
        ori = 270
        )
    ylab.autoDraw = True
    win.flip()

    # now wait until mouse is pressed
    pressed = False
    while not pressed:
        for i in range(GRID_DIM):
            for j in range(GRID_DIM):
                # let's give participant a little visual pizzaz
                if grid[i, j].contains(mouse):
                    grid[i, j].fillColor = 'red'
                else:
                    grid[i, j].fillColor = 'white'
                if mouse.isPressedIn(grid[i, j]):
                    pos, neg = i, j # save to return later
                    pressed = True # terminates `while` loop
        win.flip()

    # clean up
    for i in range(GRID_DIM):
        for j in range(GRID_DIM):
            grid[i, j].autoDraw = False # turn off autodraw
    xlab.autoDraw = False
    ylab.autoDraw = False
    win.flip() # then flip again to clear screen
    return pos + 1, neg + 1 # return to 1-indexing for Likertness
