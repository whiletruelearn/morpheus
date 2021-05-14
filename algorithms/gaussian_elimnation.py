import numpy as np
import pandas as pd


class GaussianElimnation:
    def __init__(self, A: np.ndarray, x: list, b: np.ndarray, partial_pivot=True, decimals=4):
        self.A = A
        self.x = x
        self.b = b
        self.partial_pivot = partial_pivot
        self.decimals = decimals
        self.augmented_matrix = np.hstack((A, b))
        self.m, self.n = self.augmented_matrix.shape
        self.row_ids = ["R{}".format(i) for i in range(1, self.m + 1)]

    def gaussian_elimnate(self):
        print("Initial matrix is \n")
        print(pd.DataFrame(self.augmented_matrix, columns=self.x + ["b"], index=self.row_ids))

        mat = self.augmented_matrix

        for col in range(0, self.n - 1):
            print("\n Iterating over colum {} \n".format(col + 1))
            for row in range(0, self.m):
                if col == row == 0:
                    col_max = mat[:, col].argmax()
                    if col_max != col:
                        print("\n\n  Operation R{0} <-> R{1}\n".format(col + 1, col_max + 1))
                        mat[[row, col_max], :] = mat[[col_max, row], :]
                        print(pd.DataFrame(mat, columns=self.x + ["b"], index=self.row_ids))

                if mat[row, col] != 0 and row > col:
                    mult_factor = mat[row, col] / mat[col, col]
                    print("\n\n Operaton : R{row_num} -> R{row_num} - R{col} * {mult_factor} \n".format(row_num=row + 1,
                                                                                                        mult_factor=mult_factor,
                                                                                                        col=col + 1))

                    mat[row, :] = mat[row, :] - (mult_factor * mat[col, :])
                    print(pd.DataFrame(mat, columns=self.x + ["b"], index=self.row_ids))

                mat = mat.round(decimals=self.decimals)
