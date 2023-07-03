import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch3 import v_calculation as cal


u = [1, 2, 3]
v = [4, 5, 6]
scala = 4

nu = np.array([1, 2, 3])
nv = np.array([4, 5, 6])

print("벡터 합:", cal.v_sum(u, v), "|", nu + nv, "\n")
print("벡터 차:", cal.v_sub(u, v), "|", nu - nv, "\n")
print("벡터 스칼라 곱:", cal.v_scala_mul(scala, u), "|", scala * nu, "\n")
print("벡터 원소 곱:", cal.v_mul(u, v), "|", nu * nv, "\n")
print("벡터 나눗셈:", cal.v_div(u, v), "|", nu / nv, "\n")