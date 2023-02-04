================================================================================
== 10 YARD BRAWL
================================================================================

--------------------------------------------------------------------------------
-- INTRODUCTION
--------------------------------------------------------------------------------

10 Yard Brawl is a remake of the classic football game 10 Yard Fight.
This is currently Python 2.  Will update to 3 soon.

--------------------------------------------------------------------------------
-- INSTALLATION
--------------------------------------------------------------------------------

Clone this repository to a folder on your computer.

10 Yard Brawl requires Python3 to be installed.

Install Python 3 according to your operating system's instructions,
see www.python.org for details.  These instructions were written
for Linux and OSX; Windows will be slightly different commands but
the overall idea is the same.

To install pygame, first, we want to create a virtual environment. A
virtual environment allows us to install Python libraries for just
our project.  This is handy because you won't run into conflicts if
you need different versions of different libraries for different
projects all on one computer: all projects have their own personal
version of a library.

To create a virtual environment, in your command line:

python3 -m venv env

Note that you're "python" command may be different than "python3".

Once you create your env, activate it:

source env/bin/activate

Now, your terminal prompt should change indicating that "env" is
active.

Next, install the dependencies.  These are in a file called requirements.txt.

pip3 install -r requirements.txt

At this point, the game should be able to run.

--------------------------------------------------------------------------------
-- RUNNING
--------------------------------------------------------------------------------

To run the game: 
python3 main.py

--------------------------------------------------------------------------------
-- MISC. NOTES
--------------------------------------------------------------------------------
Screen layout:
0-31: border
32-671: field
672-799: GUI

Field width: 640px (20 tiles wide)
32x32 tiles, 2 yards per tile 
-60 (top of screen) to 59 (bottom of screen) yardlines
