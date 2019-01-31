"""
Example showing for tkinter and ttk:
  -- tkinter.Tk - the main (root) window
  -- The root window's mainloop - the Event Loop

A window should pop up.  That's all for this demo.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk  # Necessary in all but this trivial example.


def main():
    root = tkinter.Tk()
    root.mainloop()

    print('Done with the Event Loop')  # Note when this line runs.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
