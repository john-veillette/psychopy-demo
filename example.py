from psychopy import visual, event, core
import os

from util.helpers import fixation_cross, ask_for_rating
from util.evaluative_state_grid import esg_fancy

STIM_FOLDER = 'cats'
fnames = os.listdir(STIM_FOLDER)
fpaths = []
for f in fnames:
	if '.png' in f:
		path_to_file = os.path.join(STIM_FOLDER, f)
		fpaths.append(path_to_file)

win = visual.Window(
    size = (1920//2, 1080//2), # in pixels
	units = 'height', # options are "norm", "height", or "pixels"
	fullscr = False,
	pos = (0, 0), # where upper left corner of window should be on screen
	allowGUI = False,
    screen = 0
)

mouse = event.Mouse(visible = True, win = win)

for stimulus in fpaths:

	fixation_cross(win, 1.)

	img = visual.ImageStim(win, stimulus, size = .5)
	img.draw()
	win.flip()
	core.wait(2)

	pos, neg = esg_fancy(win, mouse)
	print(pos, neg)
