import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch3 import m_calculation as cal

M = [[2, 7], [3, 4], [5, 2]]
N = [[1, 4], [4, -1], [2, 5]]
O = [[3, -3, 5], [-1, 2, -1]]
scala = 3

NM = np.array([[2, 7], [3, 4], [5, 2]])
NN = np.array([[1, 4], [4, -1], [2, 5]])
NO = np.array([[3, -3, 5], [-1, 2, -1]])

print("행렬 합:", cal.m_sum(M, N), "\n\n", NM + NN, "\n"`)

print("행렬 차:", cal.m_sub(M, N), "\n\n", NM - NN, "\n")

print("행렬 스칼라 곱:", cal.m_scala_mul(scala, N), "\n\n", scala * NM, "\n")

print("행렬 원소 곱:", cal.m_element_mul(M, N), "\n\n", np.multiply(NM, NN), "\n")

print("행렬 곱:", cal.m_mul(M, O), "\n\n", np.matmul(NM, NO), "\n")
