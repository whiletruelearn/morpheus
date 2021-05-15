import numpy as np
import pandas as pd
from morpheus.core.utils import log

class GaussianElimnation:
    """
    An algorithm for solving system of linear equations.
    https://en.wikipedia.org/wiki/Gaussian_elimination
    """
    def __init__(self, A: np.ndarray, x: list, b: np.ndarray, partial_pivot=True, decimals=4, use_streamlit=True):
        self.A = A
        self.x = x
        self.b = b
        self.partial_pivot = partial_pivot
        self.decimals = decimals
        self.augmented_matrix = np.hstack((A, b))
        self.m, self.n = self.augmented_matrix.shape
        self.row_ids = ["R{}".format(i) for i in range(1, self.m + 1)]
        self.U = None
        self.use_streamlit = use_streamlit

    def forward_elimnation(self):
        """
        Forward elimnation of the augmented matrix
        leading to a Upper Triangular matrix (U)
        """
        log("Initial matrix is \n", self.use_streamlit)
        log(pd.DataFrame(self.augmented_matrix, columns=self.x + ["b"], index=self.row_ids), self.use_streamlit)

        mat = self.augmented_matrix

        for col in range(0, self.n - 1):
            log("\n Iterating over column {} \n".format(col + 1), self.use_streamlit)
            for row in range(0, self.m):
                if col == row == 0:
                    col_max = mat[:, col].argmax()
                    if col_max != col:
                        log("\n\n  Operation R{0} <-> R{1}\n".format(col + 1, col_max + 1), self.use_streamlit)
                        mat[[row, col_max], :] = mat[[col_max, row], :]
                        log(pd.DataFrame(mat, columns=self.x + ["b"], index=self.row_ids), self.use_streamlit)

                if mat[row, col] != 0 and row > col:
                    mult_factor = mat[row, col] / mat[col, col]
                    log("\n\n Operaton : R{row_num} -> R{row_num} - R{col} * {mult_factor} \n".format(row_num=row + 1,
                                                                                                        mult_factor=mult_factor,
                                                                                                        col=col + 1), self.use_streamlit)

                    mat[row, :] = mat[row, :] - (mult_factor * mat[col, :])
                    log(pd.DataFrame(mat, columns=self.x + ["b"], index=self.row_ids), self.use_streamlit)

                mat = mat.round(decimals=self.decimals)
        self.U = mat

    def backward_substitution(self):
        """
        Substitute values from backward to find the
        values of unknown.

        https://algowiki-project.org/en/Backward_substitution
        """

        unknowns =  np.zeros(len(self.x))
        for r in range(len(self.x) -1 ,-1,-1):
            row = self.U[r,:self.n-1]
            b = self.U[r][self.n -1]
            if np.count_nonzero(row) == 1:

                unknowns[r] = 1
                unknowns[r] = b / np.dot(row, unknowns)
            else:

                leading_val = row[r]

                if leading_val > 0:
                    unknowns[r] = (b - np.dot(row,unknowns)) / leading_val
                else:
                    unknowns[r] = 0

        result = pd.DataFrame(np.hstack((np.array(self.x).reshape(-1,1),unknowns.reshape(-1,1))), columns = ["unknowns","root"])
        result["root"] = result.apply(lambda x : float(x["root"]),axis =1)
        log("# Solution of the Linear equation \n", self.use_streamlit)
        log(result, self.use_streamlit)
        return result

