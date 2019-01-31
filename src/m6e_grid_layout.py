"""
Example showing for tkinter and ttk:
  -- How to layout objects using a grid of rows and columns.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    # -------------------------------------------------------------------------
    # This example puts the widgets in a 3-column, 2-row grid
    # with some of the grid-places empty.  Here are the WIDGETS:
    # -------------------------------------------------------------------------

    label = ttk.Label(frame, text="Example of gridding\nrows and columns")
    entry_box = ttk.Entry(frame)

    button1 = ttk.Button(frame, text="Do you like\nyour button HERE?")
    button1['command'] = (lambda:
                          print('Do you like green eggs and ham, Sam?'))

    button2 = ttk.Button(frame, text="or HERE?")
    button2['command'] = (lambda:
                          print("I DO like green eggs and ham, Sam I am!"))

    # -------------------------------------------------------------------------
    # Here is the use of GRID with rows and columns:
    # -------------------------------------------------------------------------
    label.grid(row=0, column=0)
    entry_box.grid(row=0, column=1)
    button1.grid(row=0, column=2)
    button2.grid(row=1, column=1)

    root.mainloop()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
