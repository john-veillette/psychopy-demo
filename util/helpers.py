from psychopy import visual, core, event

def fixation_cross(win, duration):
	'''
	Presents a fixation cross for specified duration

	Parameters
	----------
	win : psychopy.visual.Window
	duration : float

	Returns
	----------
	None
	'''
	fixation = visual.TextStim(win, '+', height = .1)
	fixation.draw()
	win.flip()
	core.wait(duration)

def ask_for_rating(win):
	'''
	Asks question, returns answer character

	Parameters
	----------
	win : psychopy.visual.Window

	Returns
	---------
	key : str
	timestamp: float
		Time since the question appears 
	'''
	msg = '''
	What do you think of cat?
	Press 1 for amazing, 2 for perfect and amazing.
	'''
	txt = visual.TextStim(win, msg, height = .05)
	txt.draw()
	clock = core.Clock()
	win.callOnFlip(clock.reset)
	win.flip()
	keys = event.waitKeys(keyList = ['1', '2'], timeStamped = clock)
	key, timestamp = keys[0] # first key that was pressed
	return key, timestamp
