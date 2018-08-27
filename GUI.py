from tkinter import Tk, Canvas, Frame

SIDE = 3

class myGUI:
    def __init__(self, parent):
        self.parent = parent
        self.board = Board(SIDE, SIDE, parent)
        parent.title("A fitting title")
        parent.minsize(300,300)

class Cell:
    """
        Basic cell unit that makes up a board game.
    """

    def __init__(self, board, row, col, color="yellow"):
        self.board = board
        self.row = row
        self.col = col
        self.color = color
        self._draw(board.square(row,col),color)

    def _draw(self,dimen,color):    ## PRIVATE method
        # self.item is the id number of the Cell within the board's canvas
        self.item = self.board.canvas.create_rectangle(fill=color,*dimen)


class Board:
    """
        Basic class for setting up a board game. Probably just tic-tac-toe for now, but will
        implement to be generic later.
    """    

    def __init__(self, nrow, ncol, window):
        # TK members (Canvas, Frame, Window, etc...)
        self.nrow = nrow
        self.ncol = ncol
        self.window = window
        self.frame = Frame(window)
        self.canvas = Canvas(self.frame, width=900, height=900)

        self.setGrid(300,300)
        self.cells = self.getCells()



        # Pack elements
        self.canvas.pack()
        self.frame.pack()


    def getCells(self):
        cells = []
        for x in range(self.nrow):
            for y in range(self.ncol):
                cells.append(Cell(self, x, y))

    def run(self):
        self.window.mainloop()

    def setGrid(self,width,height):
        # width and height are pixel dimensions of ONE cell.
        # also resizes the canvas.
        self.cellWidth = width
        self.cellHeight = height
        canWid = self.ncol*width
        canHgt = self.nrow*height
        self.canvas.config(width=canWid,height=canHgt)

    def square(self,row,col):
        # returns coordinates of rectangle occupied by cell
        x = self.cellWidth * col
        y = self.cellHeight * row
        return (x,y,x+self.cellWidth,y+self.cellHeight)

root = Tk()
gui = myGUI(root)
root.mainloop()