import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ch4 import householder

# 벡터
u = [1, 0, 2, 3]

# numpy 벡터
nU = np.array([1, 0, 2, 3])

NoM = np.outer(nU, nU)
NiM = np.inner(nU, nU)
Nid = np.identity(len(nU))

print("하우스홀더 행렬:", householder.m_householder(u), "\n")
print(Nid - (2 / NiM) * NoM)
