import random
import time
import connect_engine

class Player():
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def get_color(self):
        return(self.color)

    def last_move(self):
        return((self.lastX,self.lastY))

    def update_last(self,x,y):
        self.lastX = x
        self.lastY = y

    def get_type(self):
        raise Exception('not implemented')


class AiRand(Player):
    def __init__(self,color, engine):
        super().__init__(color, engine)

    def get_move(self, moves):
        return(random.choice(moves))

    def get_type(self):
        return('random')


class Human(Player):
    def __init__(self, color, engine, renderer):
        super().__init__(color, engine)
        self.renderer = renderer

    def get_move(self, moves):
        win = self.renderer.get_window()
        maxWidth = self.renderer.get_width()

        board = self.engine.get_board()

        while True:
            alley = (win.getMouse()).getX()
            choice = int(alley // (maxWidth / 7))

            if choice in moves:
                return(choice)
            print('pick a real move')

    def get_type(self):
        return('human')


class AiMonte(Player):
    def __init__(self, color, engine, samples):
        super().__init__(color, engine)
        self.samples = samples

    def get_move(self, moves):
        children = len(moves)
        curr_samples = self.samples
        samples_per_child = curr_samples//children

        while samples_per_child != 0:
            curr_samples += 1
            samples_per_child = curr_samples//children

        print('getting move with', curr_samples)

        for child in moves:
            self.hard_rollout(child,samples_per_child)


    def hard_rollout(self,move,samples):


    def get_type(self):
        return('monte')