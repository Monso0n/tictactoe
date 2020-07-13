map = ["-"] * 9
curplayer = "X" # the first player is X, because X is cooler than O

def printmap(): #This function prints the map
    print("*****")
    for i in range(len(map)):
        print(map[i], end = '')
        if (i+1)%3==0 and i!=0:
            print('')
    print("*****")


def getInput(): #This function gets input from the console and adds the input the map
    global curplayer
    print(f"\nIt is player {curplayer}'s turn")

    while True:
        print("Pick a position from [1-9]: ")
        pos = input()

        if not pos.isnumeric():
            print("Input is not numeric!")
        elif int(pos) < 1 or int(pos) > 9:
            print("Input out of allowed range!")
        elif map[int(pos) - 1] != "-":
            print(f"Position {pos} is occupied by {map[int(pos) - 1]}")
        else:
            map[int(pos) - 1] = curplayer

            if curplayer == "X":
                curplayer = "O"
            else:
                curplayer = "X"
            break
    printmap()


#012
#345
#678
def checkMap():
    def checkVertical():
        for i in range(2):
            if map[i*3] == map[i*3 + 1] == map[i*3 + 2] and map[i*3] != "-":
                print(f"{map[i*3]} is the winner!")
                resetMap()


    def checkHorizontal():
        for i in range(2):
            if map[i] == map[i+3] == map[i+6] and map[i] != "-":
                print(f"{map[i]} is the winner!")
                resetMap()


    def checkDiagonal():
        if (map[0] == map[4] == map[8] or map[2] == map[4] == map[6]) and map[4]!="-":
            print(f"{map[4]} is the winner!")
            resetMap()

    def resetMap():
        global map
        map = ["-"] * 9
        print("\nThe map has been reset\n")
        print("NEW GAME HAS BEGUN")



    checkVertical()
    checkHorizontal()
    checkDiagonal()


def playGame():
    printmap()

    while True:
        getInput()
        checkMap()


playGame()

