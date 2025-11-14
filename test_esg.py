from psychopy import visual, event
from util.evaluative_state_grid import esg, esg_fancy

win = visual.Window(
    size =(1920//2, 1080//2), # in pixels
	units = 'height', # options are "norm", "height", or "pixels"
	fullscr = False,
	pos = (0, 0), # where upper left corner of window should be on screen
	allowGUI = False,
    screen = -1 # if multiple screens available, use the "last" one
)

mouse = event.Mouse(visible = True, win = win)
result = esg(win, mouse)
print(result)
