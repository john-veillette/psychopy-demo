# Installing PsychoPy

I recommend installing PsychoPy using `conda`. Unfortunately, `conda` will only install an [old version](https://anaconda.org/conda-forge/psychopy) of PsychoPy because the developers decided to stop maintaining a `conda` installer. But this is rarely an issue unless you are forced to interact with some of that spaghetti code the PsychoPy GUI auto-generates. In any event, I still find `conda ` to be, by far, the easiest install method if you're going to interact with PsychoPy's programming API directly.

Follow the instructions for you platform to [install conda](https://github.com/conda-forge/miniforge), and then open your Terminal (if you're on a Unix-like platform e.g. Mac or Linux) and run
```
conda create --name psychopy --channel conda-forge psychopy pyglet=1.5 python=3.9
```
This tells us `conda` to create a new environment named "psychopy", containing the `psychopy` package, version 1.5 of the `pyglet` package, and Python version 3.9, and tells it to look for these packaged on the `conda-forge` server. (Ye olde Python 3.9 and the specific version of `pyglet` are just to pick versions that play nice with PsychoPy across a number of platforms... you may be able to get away with just `conda create --name psychopy psychopy` depending on what operating system you're currently using and how `conda` has been set up... but why tempt fate?)

On Mac OS (which isn't what I'd generally recommend running your experiment code on... but to each their own), the version of PsychoPy installed by the above steps was having a problem drawing shapes. This was fixed by updating the PsychoPy version using `pip`, after initially installing it with `conda`:
```
conda activate psychopy
pip install -U psychopy==2025.2.1
```

After that's all done, you can enter your shiny new environment by running
```
conda activate psychopy
```
You should be able to run PsychoPy code from the Terminal now. You could test this out by running the `test_ecg.py` script. Change your working directory in Terminal to this folder, and then run
```
python test_esg.py
```
and see if anything fun happens.
