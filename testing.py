from tkinter import Tk, Frame
import sys

root = Tk()

side=500

def callback(event):
    print("clicked at", event.x, event.y)
    sys.stdout.flush()


# TODO
# Need to find a way to provide a width, then pack a widget into each cell, probably need a "CELL" object.
# I want it to look like a tic-tac-toe board.
# Corner's are special cases, but we'll see...
    


frame = Frame(root, width=side, height=side)
frame.bind("<Button-1>", callback)
frame.pack()






root.mainloop()
