import numpy as np
import sys
from morpheus.algorithms.gaussian_elimnation import GaussianElimnation


"""
sample augmented matrix 
=======================


    x1  x2  x3  x4  x5     b
R1   1   1   0   0   0  1300
R2   0   1   1   0   0   600
R3   0   0   1   1   0  1000
R4   0   0   0   1   1  1000
R5   1   0   0   0   1  1300
R6   0   1   0   0   1   600

Roots of the equation
=====================

x1 = 1000
x2 = 300
x3 = 300
x4 = 700
x5 = 300

Expected U
============

     1   1   0   0   0  1300
R2   0   1   1   0   0   600
R3   0   0   1   1   0  1000
R4   0   0   0   1   1  1000
R5   0   0   0   0   2   600
R6   0   0   0   0   0     0


"""

A1 = np.array([[1,1,0,0,0],
               [0,1,1,0,0],
               [0,0,1,1,0],
               [0,0,0,1,1],
               [1,0,0,0,1],
               [0,1,0,0,1]])
x1 = ["x1","x2","x3","x4","x5"]
b1 = np.array([1300, 600, 1000, 1000, 1300, 600]).reshape((6,1))
U1 = np.array([[1,1,0,0,0,1300],
                           [0,1,1,0,0,600],
                           [0,0,1,1,0,1000],
                           [0,0,0,1,1,1000],
                           [0,0,0,0,2,600],
                           [0,0,0,0,0,0]])

roots = np.array([1000,300,300,700,300])

def test_gaussian_forward_elimnation():

    g = GaussianElimnation(A=A1,x=x1,b=b1)
    g.forward_elimnation()

    assert (g.U == U1).all() == True

def test_backward_substitution():

    g = GaussianElimnation(A=A1, x=x1, b=b1)
    g.forward_elimnation()
    res = g.backward_substitution()
    assert (res["root"].values ==  roots).all() == True



