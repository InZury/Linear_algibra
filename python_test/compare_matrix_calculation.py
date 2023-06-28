import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch3 import m_calculation as cal

M = [[2, 7], [3, 4], [6, 1]]
N = [[1, 4], [4, -1], [2, 5]]
scala = 3

print("행렬 합:", cal.m_sum(M, N))
