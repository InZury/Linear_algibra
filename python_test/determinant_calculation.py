import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch6 import determinant as det

M = [[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]]
N = [[6, 3], [5, 4]]

nM = np.array([[3, 2, 0], [-1, -3, 6], [2, 3, -5]])

print("M 행렬의 행렬식:", det.det_rec(M))
print("N 행렬의 행렬식:", det.det_rec(N))

print("nM 행렬의 행렬식", np.linalg.det(nM))