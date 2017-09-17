import connect_board_renderer
import connect_engine
import connect_players
import os

import time

def play_game(p1, p2, VISUALIZE, samples_one, samples_two):
    engine = connect_engine.Engine()

    MAX_MOVES = 21

    MONTE_ONE = samples_one
    MONTE_TWO = samples_two

    if VISUALIZE:

        WINDOW_WIDTH = 700
        WINDOW_HEIGHT = 600

        renObj = connect_board_renderer.Renderer(engine, WINDOW_WIDTH, WINDOW_HEIGHT)
        renObj.draw_board()


    n = 0
    if p1 == 'Human':
        if not VISUALIZE:
            raise PlayerError('Cannot play without visualize')
        PLAYER_ONE = connect_players.Human('r', engine, renObj)
    elif p1 == 'Random AI':
        PLAYER_ONE = connect_players.AiRand('r', engine)
    elif p1 == 'Monte Carlo AI':
        PLAYER_ONE = connect_players.AiMonte('r', engine, MONTE_ONE)

    if p2 == 'Human':
        if not VISUALIZE:
            raise ValueError('Cannot play without visualize')
        PLAYER_TWO = connect_players.Human('b', engine, renObj)
    elif p2 == 'Random AI':
        PLAYER_TWO = connect_players.AiRand('b', engine)
    elif p2 == 'Monte Carlo AI':
        PLAYER_TWO = connect_players.AiMonte('b', engine, MONTE_TWO)

    players = [PLAYER_ONE, PLAYER_TWO]
    turn = 0
    # time_arr = []
    while n < MAX_MOVES:
        moves = engine.get_legal_moves()
        state = engine.is_terminal(players[1 - turn].get_color(), moves)

        if state != 0:
            # print('avg move took {0} seconds'.format(sum(time_arr)/len(time_arr)))
            break
        # start=time.time()
        move = players[turn].get_move(moves)
        # end=time.time()
        # time_arr.append(end-start)
        
        point = engine.update_board(move, players[turn].get_color())
        
        if VISUALIZE:
            renObj.update_pieces(point[0], point[1], players[turn].get_color())

        turn = 1 - turn

    if VISUALIZE:
        renObj.end()
        engine.print_final()

    return(state)


def benchmark(p1,p2,games_to_play,renderer_option,monte_sims_1,monte_sims_2,trainter=0):

    red = 0
    black = 0
    draw = 0
    total = 0
    print(games_to_play)
    print('Games played per test:', games_to_play)


    for i in range(games_to_play):
        game_result = play_game(p1, p2, renderer_option, monte_sims_1, monte_sims_2)
        if game_result == 'r':
            red += 1
        elif game_result == 'b':
            black += 1
        elif game_result == 'd':
            draw += 1
        total += 1
        print('game {0} over'.format(i))

    print('red won {0} times, {1} win rate'.format(red, round(red*100/total, 3)))
    print('black won {0} times, {1} win rate'.format(black, round(black*100/total, 3)))
    print('there were {0} draws, {1} draw rate'.format(draw, round(draw*100/total, 3)))

if __name__ == "__main__":
    benchmark('Monte Carlo AI','Monte Carlo AI',1000000,0,100,100,1)