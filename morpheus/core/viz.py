import streamlit as st
import numpy as np
import pandas as pd
from morpheus.algorithms.gaussian_elimnation import GaussianElimnation
import sys
st.title("Gauss Elimnation")

def show_gaussian_input():
    A = st.text_area("Enter your matrix A","[[-3,8],[8,-12]]")
    A = eval(A)

    if type(A) != list:
        st.write("Matrix A is not correctly formed")

    x = st.text_input("Enter your unknowns x in form of a list", "['x','y']")

    x = eval(x)

    if type(x) != list:
        st.write("Unknowns  are not correctly formed","[5,-11]")

    b = st.text_input("Enter the coefficients b ")

    b = eval(b)

    if type(b) != list:
        st.write("coefficients  are not correctly formed")

    return A, x, b

A, x, b = show_gaussian_input()

if st.button('Start elimnation'):
    A = np.array(A)
    b = np.array(b).reshape(len(b),1)
    g= GaussianElimnation(A=A, x= x, b =b, use_streamlit = True)
    g.forward_elimnation()
    g.backward_substitution()