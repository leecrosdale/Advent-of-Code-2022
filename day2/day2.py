WIN = 6
DRAW = 3
LOSS = 0

filename = './day2/data.txt'

OPPONENT_MOVES = ['A', 'B', 'C']
PLAYER_MOVES = ['X', 'Y', 'Z']
MOVE_SCORES = [1, 2, 3]
MOVE_NAMES = ['ROCK', 'PAPER', 'SCISSORS']

WIN_MOVES = [[1, 0], [0, 2], [2, 1]]


def run_part1():
    total_score = 0
    with open(filename) as fh:
        for line in fh:

            moves = line.replace('\n', '').split(' ')
            enemy_move = OPPONENT_MOVES.index(moves[0])
            player_move = PLAYER_MOVES.index(moves[1])

            print(f"{MOVE_NAMES[enemy_move]} ({moves[0]}) {str(enemy_move)} vs ({moves[1]}){MOVE_NAMES[player_move]}  "
                  f"{str(player_move)}")

            score = determine_score(enemy_move, player_move)
            total_score = total_score + score

    print("Score: " + str(total_score))


def run_part2():
    total_score = 0
    with open(filename) as fh:
        for line in fh:

            moves = line.replace('\n', '').split(' ')
            enemy_move = OPPONENT_MOVES.index(moves[0])
            result = moves[1]

            if result == 'Y':
                player_move = enemy_move
            elif result == 'X':
                player_move = 0 if enemy_move == 1 else 2 if enemy_move == 0 else 1
            else:  # RESULT IS Z
                player_move = 2 if enemy_move == 1 else 1 if enemy_move == 0 else 0

            score = determine_score(enemy_move, player_move)

            total_score = total_score + score

    print("Score: " + str(total_score))


def determine_score(enemy_move, player_move):
    if [enemy_move, player_move] in WIN_MOVES:
        score = LOSS + player_move + 1
    elif [player_move, enemy_move] in WIN_MOVES:
        score = WIN + player_move + 1
    else:
        score = DRAW + player_move + 1
    return score
