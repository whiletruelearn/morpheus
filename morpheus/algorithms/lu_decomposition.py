import numpy as np
import pandas as pd

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
        self.m, self.n = self.A.shape()


    def dolittle_method(self):
        """
        In dolittle method, diagonal matrix of Lower Triangular matrix (L) is 1.
        """
        log("## Executing Dolittle method",use_streamlit = self.use_streamlit)
        log("\nInitial matrix A \n",use_streamlit = self.use_streamlit)
        log(pd.DataFrame(self.A),use_streamlit = True)

        self.L = np.zeroes((self.m,self.m))
        for idx in range(0,self.m):
            self.L[idx][idx] = 1

        log("Setting *L* Matrix diagonal values as 1", use_streamlit = self.use_streamlit)
        log(pd.DataFrame(self.L))

        log("Setting *U* Matrix first row -> *A* Matrix first row",use_streamlit = self.use_streamlit)
        self.U[1,:] = self.A[1,:]
        log(pd.DataFrame(self.U))

        log("Setting *L* Matrix sceond column -> *A* second column /  U11",use_streamlit = self.use_streamlit)
        for j in range(1, self.m):
            self.L[j][1] = self.A[j][1] / self.U[0][0]
        log(pd.DataFrame(self.U))

        log("Update rest of *U* matrix",use_streamlit= self.use_streamlit)
        for j in range(1,self.m):
            for k in range(j,self.m):
                complement = 0
                for s in range(1,j):
                    complement += self.L[j][s] * self.U[s][k]
            log("U{j}{k} = A{j}{k} - {complement}".format(j=j,k=k,complement=complement),use_streamlit = self.use_streamlit)
            self.U[j][k] = self.A[j][k] - complement
            log(pd.DataFrame(self.U))

        log("Updating ret of the *L* matrix",use_streamlit = self.use_streamlit)
        for k in range(1, self.m):
            for j in range(k, self.m):
                denominator = self.U[k][k]
                complement = 0
                for s in range(1,k):
                    complement += self.L[j][s] * self.U[s][k]
                log("L{j}{k} = A{j}{k} - {complement}".format(j=j, k=k, complement=complement),use_streamlit=self.use_streamlit)
                self.L[j][k] = (self.A[j][k] - complement) / denominator
                log(pd.DataFrame(self.L))


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



