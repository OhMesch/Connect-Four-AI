import connect_board_renderer
import connect_engine
import connect_players
import time

def play_game(p1, p2, VISUALIZE, samples=100):
    engine = connect_engine.Engine()

    MONTE_SAMPLES = samples

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
    elif p1 == 2:
        PLAYER_ONE = connect_players.AiMonte('r', engine, MONTE_SAMPLES)

    if p2 == 0:
        if not VISUALIZE:
            raise ValueError('Cannot play without visualize')
        PLAYER_TWO = connect_players.Human('b', engine, renObj)
    elif p2 == 1:
        PLAYER_TWO = connect_players.AiRand('b', engine)
    elif p2 == 2:
        PLAYER_TWO = connect_players.AiMonte('b', engine, MONTE_SAMPLES)

    max_moves = 21
    players = [PLAYER_ONE, PLAYER_TWO]
    turn = 0


    while n < max_moves:
        moves = engine.get_legal_moves()
        state = engine.is_terminal(players[1 - turn].get_color(), moves)

        if state != 0:
            break

        move = players[turn].get_move(moves)
        point = engine.update_board(move, players[turn].get_color())
        
        if VISUALIZE:
            renObj.update_pieces(point[0], point[1], players[turn].get_color())
            time.sleep(1)

        turn = 1 - turn

    if VISUALIZE:
        renObj.end()
        engine.print_final()

    return(state)


def main():
    games_to_play = 1
    renderer_option = True

    red = 0
    black = 0
    draw = 0
    total = 0

    for i in range(games_to_play):
        result = play_game(2, 2, renderer_option)
        if result == 'r':
            red += 1
        elif result == 'b':
            black += 1
        elif result == 'd':
            draw += 1
        total += 1

        print('game {0} over'.format(i))

    print('red won {0} times, {1} win rate'.format(red, round(red*100/total, 3)))
    print('black won {0} times, {1} win rate'.format(black, round(black*100/total, 3)))
    print('there were {0} draws, {1} draw rate'.format(draw, round(draw*100/total, 3)))


def benchmark():
    games_to_play = 300
    renderer_option = False

    red = 0
    black = 0
    draw = 0
    total = 0

    print('Games played per sample:', games_to_play)
    for samples in range(1, 500):
        samples = samples * 7
        for i in range(games_to_play):
            result = play_game(1, 2, renderer_option, samples)
            if result == 'r':
                red += 1
            elif result == 'b':
                black += 1
            elif result == 'd':
                draw += 1
            total += 1

            # print('game {0} over'.format(i))


        print('Samples: {0}, percent won: {1}'.format(samples, round(black*100/total, 3)))

    # print('red won {0} times, {1} win rate'.format(red, round(red*100/total, 3)))
    # print('black won {0} times, {1} win rate'.format(black, round(black*100/total, 3)))
    # print('there were {0} draws, {1} draw rate'.format(draw, round(draw*100/total, 3)))

benchmark()