import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ch7 import inverseMatrix as inv

M = [[3, 2, 0], [-1, -3, 6], [2, 3, -5]]

nM = np.array([[3, 2, 0], [-1, -3, 6], [2, 3, -5]])

print(nM, "\n")

print("M 행렬의 역행렬:\n", inv.m_inverse(M))

print("nM 행렬의 역행렬:\n", np.linalg.inv(nM))