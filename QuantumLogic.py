#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
import math
import numpy as np
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[3]:


backend_sim = Aer.get_backend('qasm_simulator')


# In[4]:


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


# In[5]:


xCircuitLookup = {0 : quantumXzero, 1 : quantumXone, 2 : quantumXtwo, 3 : quantumXthree, 4 : quantumXfour, 5 : quantumXfive, 6 : quantumXsix, 7 : quantumXseven, 8 : quantumXeight}
yCircuitLookup = {0 : quantumYzero, 1 : quantumYone, 2 : quantumYtwo, 3 : quantumYthree, 4 : quantumYfour, 5 : quantumYfive, 6 : quantumYsix, 7 : quantumYseven, 8 : quantumYeight}
backend_sim = Aer.get_backend('qasm_simulator')

def observeSquare (square):
    x = True
    xBox = xCircuitLookup[square]
    xBox.measure(range(1),range(1))
    xjob = execute(xBox, backend_sim, shots=100)
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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




