# 역행렬 계산

def zero_mat(col, row): # 영행렬

    zero = []

    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(0)
        zero.append(sub)

    return zero

def deepcopy(M): # 깊은 복사

    if type(M[0]) == list:
        col = len(M)
        row = len(M[0])
        result = zero_mat(col, row)

        for i in range(col):
            for j in range(row):
                result[i][j] = M[i][j]
    else:
        row = len(M)
        result = []
        for i in range(row):
            result.append(M[i])
        
    return result
    
def transpose(M): # 전치 행렬

    col = len(M)
    row = len(M[0])
    result = []

    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(M[j][i])
        result.append(sub)
    
    return result

def m_scala_mul(scala, M): # 행렬의 스칼라 곱

    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(scala * M[i][j])
        result.append(sub)

    return result

def det_rec(M): # 행렬식 계산

    size = len(M)
    det = 0

    if size == 2:
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    else:
        for i in range(size):
            X = deepcopy(M)
            X = X[1:]
            xSize = len(X)

            for j in range(xSize):
                X[j] = X[j][0:i] + X[j][i+1:]
            cof = (-1) ** (i % 2)
            sub_det = det_rec(X)
            det += cof * M[0][i] * sub_det
        
    return det

def m_inverse(M): # 역행렬 계산

    size = len(M)
    X = deepcopy(M)
    C = []

    for i in range(size):
        subC = []
        rowIdx = list(range(size))
        rowIdx.remove(i)

        for j in range(size):
            colIdx = list(range(size))
            colIdx.remove(j)
            N = []

            for k in rowIdx:
                subN = []

                for l in colIdx:
                    subN.append(X[k][l])
                N.append(subN)
            Nij = det_rec(N)
            Cij = ((-1) ** (i+j)) * Nij
            subC.append(Cij)
        C.append(subC)
    adj = transpose(C)
    result = m_scala_mul(1/det_rec(X), adj)

    return result