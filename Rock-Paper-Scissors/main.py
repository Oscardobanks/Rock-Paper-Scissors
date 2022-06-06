'''
Rock-Paper-Scissors is a simple two-player game where, at a signal
players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors.
If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
In the program the two players to play the game will be the computer and the user
'''




import random
R = 'Rock'
S = 'Scissors'
P = 'Paper'
var0 = 'P > R'
var1 = 'R > S'
var2 = 'S > P'
R_P_S = ['R', 'S', 'P']
for i in R_P_S:
    user = input('Enter your option between R, S, and P:')
    if user in R_P_S:
        Computer = random.choice(R_P_S)
        print(f'Player({user}): CPU({Computer})')
        game = f'{user} > {Computer}'
        game2 = f'{Computer} > {user}'
        if game == var0 or game == var1 or game == var2:
            print('You won the game')
            break
        if game2 == var0 or game2 == var1 or game2 == var2:
            print('Computer won the game')
            break
        else:
            print('The game is a tie')
    else:
        print('Not in the options. Choose a different option')