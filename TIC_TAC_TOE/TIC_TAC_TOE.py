import random 

# GLOBAL DECLARATION
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
winner = None
gameRunning = True  

# PRINTING THE GAME BOARD 

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print("--------")
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print("--------")
    print(board[6] + " | " + board[7] + " | " + board[8] )
       
# TAKE PLAYER INPUT

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >=1 and inp <=9 and board [inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is in the spot")

# CHECK FOR WIN OR TIE 

def checkHorizontal(board):
    global winner  
    if board[0] == board[1] == board[2] and board [1] !="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board [3] !="-":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board [6] !="-":
        winner = board[6]
        return True
    
def checkColumn(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    if board[0] == board [4] == board[8]and board[0] !="-":
        winner = board[0]
        return True
    elif board[2] == board [4] == board[6]and board[2] !="-":
        winner = board[2]
        return True
    
def checkTie(board):
    if checkHorizontal(board) != checkColumn(board) != checkDiagonal(board):
        global gameRunning
        printboard(board)
        print("It is tie Match")
        gameRunning = False
    
# SWITCH PLAYER 

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else: 
        currentPlayer = "X"

def checkWin():
    if checkHorizontal(board) or checkColumn(board) or checkDiagonal(board) :
        print(f"The winner is {winner}")
    
 
# RANDOM COMPUTER CHOICE 

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)

