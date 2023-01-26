import random

random.seed()

valid_input = ['r','p','s']
game_conditions = {
    'move': valid_input,
    'beats': ['s','r','p']
}

num_player_wins = 0
num_ai_wins = 0
num_ties = 0

def game_state(player, ai) -> str:
    ret_str = 'tie'
    if player == 'r' and ai != 'r':
        ret_str = 'win' if ai == 's' else 'lose'

    elif player == 'p' and ai != 'p':
        ret_str = 'win' if ai == 'r' else 'lose'

    elif player == 's' and ai != 's':
        ret_str = 'win' if ai == 'p' else 'lose'

    return ret_str

player_move = 0
while True:
    player_move = input('Enter r/p/s for Rock, Paper, Scissors respectively\t')

    if player_move in valid_input:
        print('Ok now it is my turn')
    else: 
        print('Invalid input. Please try again')
        continue
    
    ai_move = random.choice(valid_input)
    print(f'I go {ai_move}')

    state = game_state(player_move, ai_move)

    if state == 'win':
        print('You win!')
        num_player_wins += 1
    elif state == 'tie':
        print('You tie')
        num_ties += 1
    else:
        print('You lose')
        num_ai_wins += 1

    print(f'Scores:\tYou: {num_player_wins},\tai: {num_ai_wins},\tties: {num_ties}')
    print()