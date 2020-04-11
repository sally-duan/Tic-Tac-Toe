board=[]
myset = set()
def FillInBoard():
    for i in range(1, 10):
        board.append(' ')
    for i in range(1, 10):
            positionChoice = int(input("Choose 1 to 9 on board position: "))
            while positionChoice in myset:
                positionChoice = int(input("board position is already fill. Find a new one."))                 
            
            myset.add(positionChoice)

            if i%2==0:
                board[positionChoice-1] ='X'
            else:
                board[positionChoice-1] ='O'
      
            board.append(board[positionChoice-1]) 
            print(".................")
            Display (board)          
    return board

def Display (board):
   
    if not len(board):
        print(" " + "|" + " " + "|" + " ")
        print(" " + "|" + " " + "|" + " ")
        print(" " + "|" + " " + "|" + " ")    
     
    else:
        print(board[6]+ "|" + board[7] +"|" + board[8])
        print("-" + " " + "-" + " " + "-" + " ")
        print(board[3]+ "|" + board[4] +"|" + board[5])
        print("-" + " " + "-" + " " + "-" + " ")
        print(board[0]+ "|" + board[1] +"|" + board[2])

def CleanUp(board):    
    board.clear()
    return board

def CalculateWinner(board):
    if (board[7]==board[8]==board[9]) or \
       (board[4] ==board[5]==board[6]) or\
        (board[1] ==board[2]==board[3]) or\
        (board[7] ==board[4]==board[1]) or\
        (board[8] ==board[5]==board[2]) or\
        (board[9] ==board[6]==board[3]) or\
        (board[1] ==board[5]==board[9]) or\
        (board[3] ==board[5]==board[7]):
        print("We have a winner ")
        return True
    else:
        print("We are tied. Try again!")
        return False

def PlayAgainConfirmation(board):
    answer =input ("do you want to play again. Type y if you want or N if you do not ")
    if answer == 'y':
        CleanUp(board)
        Display(board)
    else:   
        print("have a nice day")

print("Wecome to Sally's Tic Tac Toe program!")
FillInBoard()
Display(board)
CalculateWinner(board)
PlayAgainConfirmation(board)