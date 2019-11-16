
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
import math
import numpy as np
# Loading your IBM Q account(s)
#provider = IBMQ.load_account()

backend_sim = Aer.get_backend('qasm_simulator')

quantumXzero = QuantumCircuit(1, 1)
quantumXone = QuantumCircuit(1, 1)
quantumXtwo = QuantumCircuit(1, 1)
quantumXthree = QuantumCircuit(1, 1)
quantumXfour = QuantumCircuit(1, 1)
quantumXfive = QuantumCircuit(1, 1)
quantumXsix = QuantumCircuit(1, 1)
quantumXseven = QuantumCircuit(1, 1)
quantumXeight = QuantumCircuit(1, 1)
quantumYzero = QuantumCircuit(1, 1)
quantumYone = QuantumCircuit(1, 1)
quantumYtwo = QuantumCircuit(1, 1)
quantumYthree = QuantumCircuit(1, 1)
quantumYfour = QuantumCircuit(1, 1)
quantumYfive = QuantumCircuit(1, 1)
quantumYsix = QuantumCircuit(1, 1)
quantumYseven = QuantumCircuit(1, 1)
quantumYeight = QuantumCircuit(1, 1)

xCircuitLookup = {0 : quantumXzero, 1 : quantumXone, 2 : quantumXtwo, 3 : quantumXthree, 4 : quantumXfour, 5 : quantumXfive, 6 : quantumXsix, 7 : quantumXseven, 8 : quantumXeight}
yCircuitLookup = {0 : quantumYzero, 1 : quantumYone, 2 : quantumYtwo, 3 : quantumYthree, 4 : quantumYfour, 5 : quantumYfive, 6 : quantumYsix, 7 : quantumYseven, 8 : quantumYeight}
backend_sim = Aer.get_backend('qasm_simulator')

def observeSquare (square):
    x = True
    xBox = xCircuitLookup[square]
    xBox.measure(range(1),range(1))
    xjob = execute(xBox, backend_sim, shots=1)
    xresult = xjob.result()
    xcount = xresult.get_counts()
    if ('0' in xcount):
        x = False
    y = True
    yBox = yCircuitLookup[square]
    yBox.measure(range(1),range(1))
    yjob = execute(yBox, backend_sim, shots=1)
    yresult = yjob.result()
    ycount = yresult.get_counts()
    if ('0' in ycount):
        y = False
    return (x, y)

def xPlaySquare (square, xPlayed):
    xCircuitLookup[square].rx(2*np.arccos(1/(np.sqrt(2**xPlayed))) - 2*np.arccos(1/(np.sqrt(2**(xPlayed-1)))), 0)
    
def yPlaySquare (square, yPlayed):
    yCircuitLookup[square].rx(2*np.arccos(1/(np.sqrt(2**yPlayed))) - 2*np.arccos(1/(np.sqrt(2**(yPlayed-1)))), 0)

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
        xPlaySquare(position, n)
        print("x poistion =",position,"x n =",n)
        currentPlayer = "O"
    else:
        playsO[position] += 1
        n = playsO[position]
        opacityO[position] = int((1-(((2**n)-1)/(2**n)))*255)
        yPlaySquare(position, n)
        print("o poistion =",position,"o n =",n)
        currentPlayer = "X"

def observe (position):
    (x,o) = observeSquare(position)
    print("x=",x,", o=",o)
    opacityX[position] = (255, 0)[x]
    opacityO[position] = (255, 0)[o]
    if (x or o):
        playableSlots[position] = False

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

def printBoard():
    global playsX, playsO
    print("      ------------GAME-------------")
    print("X:",playsX[0],"|O",playsO[0],"    ", "X:",playsX[1],"|O",playsO[1],"    ", "X:",playsX[2],"|O",playsO[2],"    ")
    print("")
    print("X:",playsX[3],"|O",playsO[3],"    ", "X:",playsX[4],"|O",playsO[4],"    ", "X:",playsX[5],"|O",playsO[5],"    ")
    print("")
    print("X:",playsX[6],"|O",playsO[6],"    ", "X:",playsX[7],"|O",playsO[7],"    ", "X:",playsX[8],"|O",playsO[8],"    ")
    print("")


while(isWin() == ""):
    command = input("Command (place or observe): ")
    place = input("Enter position: ")
    printBoard()

