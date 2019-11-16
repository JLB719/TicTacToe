# Board
# 0|1|2
# -----
# 3|4|5
# -----
# 6|7|8

opacityX = [255, 255, 255, 255, 255, 255, 255, 255, 255]
opacityO = [255, 255, 255, 255, 255, 255, 255, 255, 255]
playsX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
playsO = [0, 0, 0, 0, 0, 0, 0, 0, 0]
currentPlayer = "X"
playableSlots = [True,True,True,True,True,True,True,True,True]

def place (position):
    global currentPlayer
    global opacityX
    global opacityO
    global playsX
    global playsO
    #Assuming they cannot place in a taken position
    if (currentPlayer == "X"):
        playsX[position] += 1
        n = playsX[position]
        opacityX[position] = int((1-(((2**n)-1)/(2**n)))*255)
        #TODO Jake's qubit gate stuff
        #xPlaySquare(position, n)
        currentPlayer = "O"
    else:
        playsO[position] += 1
        n = playsO[position]
        opacityO[position] = int((1-(((2**n)-1)/(2**n)))*255)
        #TODO Jake's qubit gate stuff
        #position[x]   xPlaySquare(position, n)
        currentPlayer = "X"

def observe (position):
    #(x,o) = observeSquare(position)
    (x,o) = (True, True)
    opacityX[position] = (255, 0)[x]
    opacityO[position] = (255, 0)[o]
    if (x or o):
        playableSlots[position] = False


def entangle (position1, position2):
    currentPlayer = currentPlayer

def renderBoard ():
    

    currentPlayer = currentPlayer
    #render opacityX
    #render opacityO
    #if either is
    #render entanglement

def isWin():
    global opacityX, opacityO
    winStr = ""
    if ((opacityX[0] == 0) and (opacityX[1] == 0) and (opacityX[2] == 0)):
        winStr += " X wins "
    elif ((opacityX[3] == 0) and (opacityX[4] == 0) and (opacityX[5] == 0)):
        winStr += " X wins "
    elif ((opacityX[6] == 0) and (opacityX[7] == 0) and (opacityX[8] == 0)):
        winStr += " X wins "
    elif ((opacityX[0] == 0) and (opacityX[3] == 0) and (opacityX[6] == 0)):
        winStr += " X wins "
    elif ((opacityX[1] == 0) and (opacityX[4] == 0) and (opacityX[7] == 0)):
        winStr += " X wins "
    elif ((opacityX[2] == 0) and (opacityX[5] == 0) and (opacityX[8] == 0)):
        winStr += " X wins "
    elif ((opacityX[0] == 0) and (opacityX[4] == 0) and (opacityX[8] == 0)):
        winStr += " X wins "
    elif ((opacityX[2] == 0) and (opacityX[4] == 0) and (opacityX[6] == 0)):
        winStr += " X wins "
    
    if ((opacityO[0] == 0) and (opacityO[1] == 0) and (opacityO[2] == 0)):
        winStr += " O wins "
    elif ((opacityO[3] == 0) and (opacityO[4] == 0) and (opacityO[5] == 0)):
        winStr += " O wins "
    elif ((opacityO[6] == 0) and (opacityO[7] == 0) and (opacityO[8] == 0)):
        winStr += " O wins "
    elif ((opacityO[0] == 0) and (opacityO[3] == 0) and (opacityO[6] == 0)):
        winStr += " O wins "
    elif ((opacityO[1] == 0) and (opacityO[4] == 0) and (opacityO[7] == 0)):
        winStr += " O wins "
    elif ((opacityO[2] == 0) and (opacityO[5] == 0) and (opacityO[8] == 0)):
        winStr += " O wins "
    elif ((opacityO[0] == 0) and (opacityO[4] == 0) and (opacityO[8] == 0)):
        winStr += " O wins "
    elif ((opacityO[2] == 0) and (opacityO[4] == 0) and (opacityO[6] == 0)):
        winStr += " O wins "

    return winStr

print("Current player = " + currentPlayer + ", is equal to x? " + (("True","False")[(currentPlayer == "X")]))
#player X
place(4)
#Player Y
place(4)
#player X
place(8)
place(4)


#gameboard
print("")
print("")
print("      ------------GAME-------------")
print("X:",playsX[0],"|O",playsO[0],"    ", "X:",playsX[1],"|O",playsO[1],"    ", "X:",playsO[2],"|O",playsO[2],"    ")
print("")
print("X:",playsX[3],"|O",playsO[3],"    ", "X:",playsX[4],"|O",playsO[4],"    ", "X:",playsO[5],"|O",playsO[5],"    ")
print("")
print("X:",playsX[6],"|O",playsO[6],"    ", "X:",playsX[7],"|O",playsO[7],"    ", "X:",playsO[8],"|O",playsO[8],"    ")
print("")


observe(0)
observe(1)
observe(2)
print(opacityX,", ",opacityO)
print(isWin())

