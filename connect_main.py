import connect_board_renderer
import connect_engine
import connect_players
import time

def play_game(p1,p2,VISUALIZE):

    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 600

    if VISUALIZE:
        renObj = connect_board_renderer.Renderer(WINDOW_WIDTH, WINDOW_HEIGHT)
        renObj.draw_board()
        window = renObj.get_window()

    n=0

    game_board=[['0' for x in range(7)] for y in range(6)]

    if p1 == 0:
        if not VISUALIZE:
            raise PlayerError('Cannot play without visualize')
        PLAYER_ONE = connect_players.Human('r',VISUALIZE)
    elif p1 == 1:
        PLAYER_ONE = connect_players.AiRand('r',VISUALIZE)

    if p2 == 0:
        if not VISUALIZE:
            raise ValueError('Cannot play without visualize')
        PLAYER_TWO = connect_players.Human('b',VISUALIZE)
    elif p2 == 1:
        PLAYER_TWO = connect_players.AiRand('b',VISUALIZE)    

    engine = connect_engine.Engine()

    while n < 21:
        if PLAYER_ONE.is_human():
            move_one = PLAYER_ONE.get_move(game_board,window,WINDOW_WIDTH)
        else:
            move_one = PLAYER_ONE.get_move(game_board)
        point= engine.update_board(game_board,move_one,PLAYER_ONE.get_color(),VISUALIZE)
        if VISUALIZE:
            renObj.update_pieces(game_board,point[0],point[1],PLAYER_ONE.get_color())
        if engine.board_eval(game_board,PLAYER_ONE.get_color()):
            print('Player 1 has won')
            if VISUALIZE:
                time.sleep(3)
            break

        if PLAYER_TWO.is_human():
            move_two = PLAYER_TWO.get_move(game_board,window,WINDOW_WIDTH)
        else:
            move_two = PLAYER_TWO.get_move(game_board)
        point = engine.update_board(game_board,move_two,PLAYER_TWO.get_color(),VISUALIZE)
        if VISUALIZE:
            renObj.update_pieces(game_board,point[0],point[1],PLAYER_TWO.get_color())
        if engine.board_eval(game_board,PLAYER_TWO.get_color()):
            print('Player 2 has won')
            if VISUALIZE:
                time.sleep(3)
            break
    if VISUALIZE:
        window.close()

        for line in game_board:
            print(line)

play_game(1,1,False)