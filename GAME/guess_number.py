import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_game ():
        nonlocal name
        nonlocal player_wins
 
        playerchoice = input(
            f'\n{name}, Guess which number I\'s m thinking of ..... 1,2, or 3: \n\n'
        )

        if playerchoice not in ['1', '2', '3']:
            print(f'\n{name}, Please Enter 1 ,2, 3')
            return play_game ()
        
        player = int(playerchoice)

        computerchoice = random.choice('123')
        computer = int(computerchoice)

        print(f'\n {name}, you chose {playerchoice}.')
        print(f'\n I was thinking about the number {computerchoice}' )

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins +=1
                print(f'\n{name}, you win !')
            else:
                print(f'sorry,{name} , Better luck next time')
            
        result = decide_winner(player,computer)
        print(result)

        nonlocal game_count
        game_count +=1

        print(f'\n Game count: {game_count}')
        print(f'\n {name}, wins : {player_wins}')
        print(f'\n Your Winning Percentage: {player_wins/game_count:.2%}')
        print(f'\n Play again, {name}?\n')

        while True:
            playagain = input('\nY for Yes \nQ for Quit  \n')
            if playagain.lower() not in ['y','q']:
             continue
            else:
                break
        if playagain.lower() == 'y':
            return guess_number()
        else:
            print('\n Thanks for playing')
            sys.exit(f'\n Bye, {name}')
    return play_game()
    


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description= 'Game expirence.'
    )

    parser.add_argument(
        '-n','--name',metavar='name',
        required=True, help= 'The name of the person playing the game.'
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number