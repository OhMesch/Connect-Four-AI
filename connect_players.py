import random
import time
import connect_engine

class Player():
    def __init__(self,color,VIS):
        self.color = color
        self.engine = connect_engine.Engine()
        self.VIS = VIS

    def get_color(self):
        return(self.color)

    def last_move(self):
        return((self.lastX,self.lastY))

    def update_last(self,x,y):
        self.lastX = x
        self.lastY = y

class AiRand(Player):
    def __init__(self,color,VIS):
        super().__init__(color,VIS)

    def get_move(self,board):
        choice = 7
        while not self.engine.valid_move(board,choice):
            choice = random.randint(0,6)
            if self.engine.valid_move(board,choice):
                if self.VIS:
                    time.sleep(1)
                return(choice)

    def is_human(self):
        return(False)

class Human(Player):
    def __init__(self,color,VIS):
        super().__init__(color,VIS)

    def get_move(self,board,win,maxWidth):
        choice = 7
        while not self.engine.valid_move(board,choice):
            alley=(win.getMouse()).getX()
            choice=int(alley//(maxWidth/7))
            if self.engine.valid_move(board,choice):
                return(choice)

    def is_human(self):
        return(True)