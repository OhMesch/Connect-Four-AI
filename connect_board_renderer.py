import graphics 
from graphics import *

class Renderer():
    def __init__(self, width=700, height=600):
        self.width = width
        self.height = height
        self.win = GraphWin("Game Board", width, height)
        self.win.setBackground("blue")

    def update(self):
        self.win.update()


    def get_window(self):
        return(self.win)


    def draw_board(self):
        for i in range(0, 6): #Determines size of terrain
            horLines = Line(Point(0, i*self.height/6),Point(self.width, i*self.height/6))
            horLines.setOutline('black')
            horLines.draw(self.win)

        for j in range(0, 7):
            verLines = Line(Point(j*self.width/7, 0),Point(j*self.width/7, self.height))
            verLines.setOutline('black')
            verLines.draw(self.win)

        for y in range(0,6):
            for x in range(0,7):
                slot = Circle(Point(x*self.width/7+50,y*self.height/6+50),37.5)
                slot.setFill("white")
                slot.draw(self.win)

    def update_pieces(self,board,x,y,color):
        pointY = y*self.height/6
        pointX = x*self.width/7
        piece = Circle(Point(pointX+50,pointY+50),37.5)
        if color == 'r':
            piece.setFill("red")
        else:
            piece.setFill("black")
        piece.draw(self.win)

class Menu(): #CHANGE TO SELF. WIDTH AND HIEGHT
    def __init__(self,window):
        self.window = window

        skyBlue = color_rgb(135,206,250)
        royalBlue = color_rgb(65,105,225)

        self.menu = Rectangle(Point(.2*500,.15*500),Point(.8*500,.8*500))
        self.menu.setFill(skyBlue)
        self.menu.setOutline(skyBlue)

        self.save = Rectangle(Point(.25*500,.2*500),Point(.75*500,.35*500))
        self.save.setOutline(royalBlue)
        self.save.setFill(royalBlue)

        self.saveTxt = Text(Point(.50*500,.275*500), "SAVE")
        self.saveTxt.setSize(30)
        self.saveTxt.setFace("helvetica")
        self.saveTxt.setStyle("bold")

        self.load = Rectangle(Point(.25*500,.4*500),Point(.75*500,.55*500))
        self.load.setOutline(royalBlue)
        self.load.setFill(royalBlue)

        self.loadTxt = Text(Point(.50*500,.475*500), "LOAD")
        self.loadTxt.setSize(30)
        self.loadTxt.setFace("helvetica")
        self.loadTxt.setStyle("bold")

        self.quit = Rectangle(Point(.25*500,.6*500),Point(.75*500,.75*500))
        self.quit.setOutline(royalBlue)
        self.quit.setFill(royalBlue)

        self.quitTxt = Text(Point(.50*500,.675*500), "QUIT")
        self.quitTxt.setSize(30)
        self.quitTxt.setFace("helvetica")
        self.quitTxt.setStyle("bold")

    def openMenu(self):
        self.menu.draw(self.window)
        self.save.draw(self.window)
        self.saveTxt.draw(self.window)
        self.load.draw(self.window)
        self.loadTxt.draw(self.window)
        self.quit.draw(self.window)
        self.quitTxt.draw(self.window)

    def closeMenu(self):
        self.menu.undraw()
        self.save.undraw()
        self.saveTxt.undraw()
        self.load.undraw()
        self.loadTxt.undraw()
        self.quit.undraw()
        self.quitTxt.undraw()