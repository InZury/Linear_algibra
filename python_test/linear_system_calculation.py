import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ch5 import gauss_jordan_elimination as gje

M = [[3, 1, 2], [2, 6, -1], [4, 0, -1]]
u = [5, 1, 3]

nM = np.array([[3, 1, 2], [2, 6, -1], [4, 0, -1]])
nu = np.array([[5], [1], [3]])

print("가우스 조르단 소거법:", gje.gje(M, u), "\n\n", np.linalg.solve(nM, nu))