import numpy as np
from scipy.linalg import toeplitz
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ch4 import var_matrix as var
from ch3 import m_calculation as cal
from ch2 import zero_mat as zero

# 행렬
M = [[1, 5], [3, 4], [6, 2]]
N = [[1, 0, 2], [0, 2, 1], [2, 1, 1]]

# 토플리츠 행렬
tM = [1, 0, -2, -4]
tN = [1, 3, 5, 7, 9]

# 행렬 제곱 복제
MM = M

# 대각 행렬
eN = var.m_diag_element(N)
dN = var.e_diag(eN)

# numpy 행렬
NM = np.array([[1, 5], [3, 4], [6, 2]])
NN = np.array([[1, 0, 2], [0, 2, 1], [2, 1, 1]])

# numpy 대각 행렬 원소
NdN = np.diag(NN)

print("전치 행렬:", var.m_transpose(M), "\n\n", np.transpose(M), "\n\n", NM.T, "\n")
print("전치 행렬 대칭 비교:", N, "\n\n", var.m_transpose(N), "\n\n", "대칭:", N == var.m_transpose(N), "\n\n", NN == np.transpose(NN), "\n")

print("대칭 행렬 거듭 제곱:")

for i in range(2, 10):
    MM = cal.m_mul(MM, M)
    print("행렬 M의", i, "제곱은", MM)
print("\n")

print("대각 행렬:", var.m_diag(N), " 대각 행렬의 원소:", eN, "\n")
print("np 대각 행렬:\n", np.diag(NdN), "\n\n", "np 대각 행렬의 원소:", NdN, "\n")

print("대각 원소 행렬 변환:", dN, "\n")

print("N * dN 대각 행렬 곱:", cal.m_mul(N, dN), "\n")
print("dN * N 대각 행렬 곱:", cal.m_mul(dN, N), "\n\n`")

print("N * dN 대각 행렬 곱:\n", np.matmul(NN, np.diag(NdN)), "\n")
print("dN * N 대각 행렬 곱:\n", np.matmul(np.diag(NdN), NN), "\n\n")

print("N 행렬의 단위 행렬:", var.m_identity(len(N)), "\n\n", np.identity(len(N)), "\n\n")

print("영 행렬:", zero.zero_mat(3, 2), "\n\n", np.zeros((3, 2)), "\n\n")

print("상 삼각 행렬:", var.m_utri(N), "\n\n", np.triu(NN), "\n\n")
print("하 삼각 행렬:", var.m_ltri(N), "\n\n", np.tril(NN), "\n\n")

print("토플리츠 행렬:", var.m_toeplitz(tM, tN), "\n\n", toeplitz(tM, tN), "\n\n")

print("상 이중 대각 행렬", var.m_upper_bidiag(N), "\n\n", np.diag(NdN) + np.diag(np.diag(NN, k = 1), k = 1), "\n\n")
print("하 이중 대각 행렬", var.m_lower_bidiag(N), "\n\n", np.diag(NdN) + np.diag(np.diag(NN, k = -1), k = -1), "\n\n")
