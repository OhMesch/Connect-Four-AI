import connect_players

class Engine():
    def board_eval(self,board,color):
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

    def update_board(self,board,move,color,output=False):
        for y in range(6)[::-1]:
            if board[y][move]=='0':
                board[y][move] = color
                break
        if output:
            return(move,y)

    def valid_move(self,board,move):
        if move < 0 or move >6:
            return(False)
        if board[0][move] == '0':
            return(True)
        else:
            return(False)