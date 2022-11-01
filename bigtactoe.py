print("Welcome to Big-Tac-Toe")

def printgrid(board): # prints the table
    for i in range(4):
        print("+-------+-------+-------+")
        if i == 3:
            break
        for j in range(3):
            if j != 1:
                print("|       |       |       |")
            else:
                print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")

          
def addToInputsArr(num, XorO): # adds inputs to the table
    if 1 <= num <= 3:
        if type(inputs[0][num-1]) == int:
            inputs[0][num-1] = XorO
        else:
            while type(inputs[0][num-1]) != int:
                print("Value already in that position, try again")
                while True:
                    try:
                        num = int(input(f"(Enter Position) {XorO}:"))
                    except ValueError:
                        print("Not an integer, try again")
                    else:
                        break
            inputs[0][num-1] = XorO
    
    elif 4 <= num <= 6:
        if type(inputs[1][(num-3)-1]) == int:
            inputs[1][(num-3)-1] = XorO
        else:
            while type(inputs[1][(num-3)-1]) != int:
                print("Value already in that position, try again")
                while True:
                    try:
                        num = int(input(f"(Enter Position) {XorO}:"))
                    except ValueError:
                        print("Not an integer, try again")
                    else:
                        break
            inputs[1][(num-3)-1] = XorO
    
    elif 7 <= num <= 9:
        if type(inputs[2][((num-3)-3)-1]) == int:
            inputs[2][((num-3)-3)-1] = XorO
        else:
            while type(inputs[2][((num-3)-3)-1]) != int:
                print("Value already in that position, try again")
                while True:
                    try:
                        num = int(input(f"(Enter Position) {XorO}:"))
                    except ValueError:
                        print("Not an integer, try again")
                    else:
                        break
            inputs[2][((num-3)-3)-1] = XorO
    else:
        while (num < 1) or (num > 9):
            print("Position out of range, try again")
            while True:
                try:
                    num = int(input(f"(Enter Position) {XorO}:"))
                except ValueError:
                    print("Not an integer, try again")
                else:
                    break
                
        addToInputsArr(num, XorO)

       
def winbool():          # checks if any player has won
    for i in range(3):
        if inputs[i][0] == inputs[i][1] == inputs[i][2]:
            return True
        elif inputs[0][i] == inputs[1][i] == inputs[2][i]:
            return True
        elif inputs[0][0] == inputs[1][1] == inputs[2][2]:
            return True
        
        elif inputs[2][0] == inputs[1][1] == inputs[0][2]:
            return True
        
    return False
    
        
                

def main():
    global win
    win = False
    global inputs
    inputs= [[1,2,3],
             [4,5,6],
             [7,8,9]
    ]
    printgrid(inputs)
    print("Player 1 is X")
    print("Player 2 is O\n")
    while win is False:
        while True:
            try:
                x = int(input("(Enter Position) X:"))
            except ValueError:
                print("Not an integer, try again")
            else:
                break
        addToInputsArr(x,"X")
        printgrid(inputs)
        print("\n")
        
        win = winbool()
        if win is True:
            print("X wins!")
            break
        
        draw = True
        
        for i in inputs:
            if (win is False) and all(isinstance(j, str) for j in i):
                pass
            else:
                draw = False
        
        if draw is True:
            print("Draw!")
            break
        
        
        while True:
            try:
                o = int(input("(Enter Position) O:"))
            except ValueError:
                print("Not an integer, try again")
            else:
                break
        addToInputsArr(o,"O")
        printgrid(inputs)
        print("\n")
        
        win = winbool()
        if win is True:
            print("O wins!")
        draw = True
        
        for i in inputs:
            if (win is False) and all(isinstance(j, str) for j in i):
                pass
            else:
                draw = False
        
        if draw is True:
            print("Draw!")
            break
        
if __name__ == "__main__":
    main()