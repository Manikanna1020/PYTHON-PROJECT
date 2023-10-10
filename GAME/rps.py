import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count=0
    player_wins=0
    python_wins=0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        
        playerchoice = input(f'\n{name}, Enter \n1 for Rock \n2 for Paper \n3 for Scissors \n\n')

        if playerchoice not in ['1','2','3']:
            print(f'\n{name}, Please Enter 1,2, or 3')
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice) 

        print(f'\n{name},you chose {str(RPS(player)).replace("RPS."," ").title()}. \n')
        print(f'\npython chose {str(RPS(computer)).replace("RPS."," ").title()}. \n')

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computerchoice

            if player == 1 and computer== 3 :
                  player_wins +=1
                  print('\nYou win')
            elif player == 2 and computer ==1 :
                player_wins +=1
                print('\nYou win')
            elif player ==3 and computer==2:
                player_wins +=1
                print('\nYou win')
            elif player == computer:
                player_wins +=1
                print('\nTie game')
            else:
                print('\nYou lose')
        
        result = decide_winner(player,computer)
        print (result)

        nonlocal game_count
        game_count +=1

        print(f'\n Game count: {game_count}')
        print(f'\n {name}, wins : {player_wins}')
        print(f'\n python wins : {python_wins}')

        print(f'\n Play again, {name}?')

        while True:
            playagain = input('\nY for Yes \nQ for Quit \n')
            if playagain.lower() not in ['y','q']:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return play_rps()
        else:
            print('\n Thanks for playing')
            sys.exit(f'\n BYE, {name}')
    return play_rps()
    
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

rps(args.name)
    


            


