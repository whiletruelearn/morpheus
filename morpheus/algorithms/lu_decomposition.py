import numpy as np
import pandas as pd
from morpheus.core.utils import log

class LUDecomposition:

    def __init__(self,  A: np.ndarray, decomposition_method : str, use_streamlit=True):
        """
        For a matrix of size mxn , LU decomposition gives a
        lower triangular matrirx L of size mxm
        and upper triangular matrix of size mxn
        """

        self.A = A
        self.decomposition_method = decomposition_method
        self.use_streamlit = use_streamlit
        self.L = None
        self.U = None
        self.m, self.n = self.A.shape


    def dolittle_method(self):
        """
        In dolittle method, diagonal matrix of Lower Triangular matrix (L) is 1.
        """
        log("## Executing Dolittle method",use_streamlit = self.use_streamlit)
        log("\nInitial matrix A \n",use_streamlit = self.use_streamlit)
        log(pd.DataFrame(self.A),use_streamlit = True)

        self.L = np.zeros((self.m,self.m))
        self.U = np.zeros((self.m,self.m))
        for idx in range(0,self.m):
            self.L[idx][idx] = 1

        log("Setting *L* Matrix diagonal values as 1", use_streamlit = self.use_streamlit)
        log(pd.DataFrame(self.L))

        log("Setting *U* Matrix first row -> *A* Matrix first row",use_streamlit = self.use_streamlit)
        self.U[0,:] = self.A[0,:]
        log(pd.DataFrame(self.U))

        for j in range(1, self.m):
            log("Setting *L* Matrix First column -> *A* first column /  U11", use_streamlit=self.use_streamlit)
            self.L[j][0] = self.A[j][0] / self.U[0][0]
            log(pd.DataFrame(self.L))


        log("Update rest of *U* matrix",use_streamlit= self.use_streamlit)
        log("U \n")
        log(pd.DataFrame(self.U))
        log("A \n")
        log(pd.DataFrame(self.A))
        for j in range(1,self.m):
            for k in range(1,self.m):
                complement = 0
                complement_str = ""
                for s in range(0,j):
                    complement += self.L[j][s] * self.U[s][k]
                    complement_str += "L[{j}][{s}] * U[{s}][{k}] + ".format(j=j,s=s,k=k)
                log("U{j}{k} = A{j}{k} - {complement}".format(j=j,k=k,complement=complement_str),use_streamlit = self.use_streamlit)
                log("U{j}{k} = A{j}{k} - {complement}".format(j=j, k=k, complement=complement),
                    use_streamlit=self.use_streamlit)
                self.U[j][k] = self.A[j][k] - complement
                log(pd.DataFrame(self.U))


        log("Updating ret of the *L* matrix",use_streamlit = self.use_streamlit)
        log("L\n")
        log(self.L)
        for k in range(1, self.m):
            for j in range(k+1, self.m):
                denominator = self.U[k][k]
                complement = 0
                complement_str = ""
                for s in range(0,k):
                    complement += self.L[j][s] * self.U[s][k]
                    complement_str += "L[{j}][{s}] * U[{s}][{k}] + ".format(j=j, s=s, k=k)
                log("L{j}{k} = (A{j}{k} - {complement} ) / {denom} ".format(j=j, k=k, complement=complement_str, denom = denominator),use_streamlit=self.use_streamlit)
                self.L[j][k] = (self.A[j][k] - complement) / denominator
                log(pd.DataFrame(self.L))

        log("Update rest of *U* matrix", use_streamlit=self.use_streamlit)
        log("U \n")
        log(pd.DataFrame(self.U))
        log("A \n")
        log(pd.DataFrame(self.A))
        for j in range(1, self.m):
            for k in range(1, self.m):
                complement = 0
                complement_str = ""
                for s in range(0, j):
                    complement += self.L[j][s] * self.U[s][k]
                    complement_str += "L[{j}][{s}] * U[{s}][{k}] + ".format(j=j, s=s, k=k)
                log("U{j}{k} = A{j}{k} - {complement}".format(j=j, k=k, complement=complement_str),
                    use_streamlit=self.use_streamlit)
                log("U{j}{k} = A{j}{k} - {complement}".format(j=j, k=k, complement=complement),
                    use_streamlit=self.use_streamlit)
                self.U[j][k] = self.A[j][k] - complement
                log(pd.DataFrame(self.U))


    def crout_method(self):
        """
        In crout method, diagonal matrix of Upper Triangular matrix (U) is 1.
        """
        pass

    def cholesky_method(self):
        """
        If matrix is semi positive definite, A could be decomposed as
        LU where U = Transpose of L. This is the most efficient form
        of decomposition, as we can form U just by transposing L.
        """
        pass

    def decompose(self):
        if self.decomposition_method == "dolittle":
            self.dolittle_method()
        elif self.decomposition_method == "crout":
            self.crout_method()
        elif self.decomposition_method == "cholesky":
            self.cholesky_method()



