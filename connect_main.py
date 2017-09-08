import connect_board_renderer
import connect_engine
import connect_players
import time

def play_game(p1, p2, VISUALIZE):
    engine = connect_engine.Engine()

    if VISUALIZE:
        WINDOW_WIDTH = 700
        WINDOW_HEIGHT = 600

        renObj = connect_board_renderer.Renderer(engine, WINDOW_WIDTH, WINDOW_HEIGHT)
        renObj.draw_board()


    n = 0
    if p1 == 0:
        if not VISUALIZE:
            raise PlayerError('Cannot play without visualize')
        PLAYER_ONE = connect_players.Human('r', engine, renObj)
    elif p1 == 1:
        PLAYER_ONE = connect_players.AiRand('r', engine)

    if p2 == 0:
        if not VISUALIZE:
            raise ValueError('Cannot play without visualize')
        PLAYER_TWO = connect_players.Human('b', engine, renObj)
    elif p2 == 1:
        PLAYER_TWO = connect_players.AiRand('b', engine)    

    max_moves = 21
    players = [PLAYER_ONE, PLAYER_TWO]
    turn = 0


    while n < max_moves:
        state = engine.is_terminal(players[1 - turn].get_color())
        moves = engine.get_legal_moves()

        if state != 0 or len(moves) == 0:
            break

        move = players[turn].get_move(moves)
        point = engine.update_board(move, players[turn].get_color())
        
        if VISUALIZE:
            renObj.update_pieces(point[0], point[1], players[turn].get_color())
            time.sleep(.01)

        turn = 1 - turn

    if VISUALIZE:
        renObj.end()
        engine.print_final()

    return(state)


def main():
    games_to_play = 100000
    renderer_option = True

    red = 0
    black = 0
    total = 0

    for i in range(games_to_play):
        result = play_game(1, 1, renderer_option)
        if result == 'r':
            red += 1
        elif result == 'b':
            black += 1
        total += 1

    print('red won {0} times, {1} win rate'.format(red, round(red*100/total, 3)))
    print('black won {0} times, {1} win rate'.format(black, round(black*100/total, 3)))
    print('there were {0} draws, {1} draw rate'.format(total-black-red, round((total-black-red)*100/total, 3)))

main()