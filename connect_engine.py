import connect_players

class Engine():
    def __init__(self):
        self.board = [['0' for x in range(7)] for y in range(6)]
        self.stack = []


    def print_final(self):
        for i in self.board:
            print(i)


    def is_terminal(self, color, moves):
        if len(moves) == 0:
            return('d')
        board = self.board
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x]!=color:
                    continue
                left = False
                right = False
                up = False
                if x <= 3:
                    right =True
                if x >=3:
                    left=True
                if y >= 3:
                    up=True
                if left:
                    if board[y][x]==board[y][x-1]==board[y][x-2]==board[y][x-3]:
                        return(color)
                if left and up:
                    if board[y][x]==board[y-1][x-1]==board[y-2][x-2]==board[y-3][x-3]:
                        return(color)
                if up:
                    if board[y][x]==board[y-1][x]==board[y-2][x]==board[y-3][x]:
                        return(color)
                if up and right:
                    if board[y][x]==board[y-1][x+1]==board[y-2][x+2]==board[y-3][x+3]:
                        return(color)
                if right:
                    if board[y][x]==board[y][x+1]==board[y][x+2]==board[y][x+3]:
                        return(color)
        return(0)


    def get_board(self):
        return self.board


    def push_move(self,move,color):
        self.stack.append(move)
        self.update_board(move,color)


    def pop_move(self):
        move = self.stack.pop()
        self.undo_move(move)


    def update_board(self, move, color):
        board = self.board
        for y in range(6)[::-1]:
            if board[y][move]=='0':
                board[y][move] = color
                break
        return(move,y)


    def undo_move(self, move):
        for y in range(6):
            if self.board[y][move] != '0':
                self.board[y][move] = '0'
                break


    def valid_move(self, move):
        board = self.board
        if move < 0 or move > 6:
            return(False)
        if board[0][move] == '0':
            return(True)
        else:
            return(False)


    def invert_color(self,color):
        if color == 'r':
            return('b')
        else:
            return('r')

    def get_legal_moves(self):
        legal = []
        for i in range(7):
            if self.valid_move(i):
                legal.append(i)
        return legal
