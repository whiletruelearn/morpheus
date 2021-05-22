import numpy as np
import sys
from morpheus.algorithms.lu_decomposition import  LUDecomposition


"""
sample Matrix
=======================


 [[2,-1, -2],
  [-4,6,3],
  [-4,-2,8]]

Expected L 
============

[[1,0,0],
 [-2,1,0],
 [-2,-1,1]]
 
Expected U
==========

[[2,-1,-2],
 [0,4,-1],
 [0,0,3]]

"""

A1 = np.array([[2,-1, -2],
                [-4,6,3],
                [-4,-2,8]])

L1 = np.array([[1,0,0],
               [-2,1,0],
               [-2,-1,1]])

U1 = np.array([[2,-1,-2],
               [0,4,-1],
               [0,0,3]])



def test_do_little_decompsition():
    lu = LUDecomposition(A = A1,decomposition_method ="dolittle",use_streamlit = False )
    lu.decompose()
    assert (lu.L == L1).all() == True
    assert (lu.U == U1).all() == True
    assert (lu.L @ lu.U == A1).all() == True




if __name__ == "__main__":
    test_do_little_decompsition()
