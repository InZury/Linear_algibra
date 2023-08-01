# 내적 계산

def innerProduct(u, v): # 벡터의 내적

    size = len(u)
    result = 0

    for i in range(size):
        result += u[i] * v[i]
    
    return result

def transpose(M): # 전치 행렬
    
    col = len(M)
    row = len(M[0])
    result = []

    for i in range(row):
        sub = []
        for j in range(col):
            sub.append(M[j][i])
        result.append(sub)
    
    return result

def vNorm(u): # 벡터의 노름
    
    row = len(u)
    result = 0

    for i in range(row):
        result += u[i]**2
    
    result = result ** 0.5

    return result

def normalize(u): # 벡터의 정규화
    
    row = len(u)
    result = []

    for i in range(row):
        result.append(u[i] / vNorm(u))

    return result

def qrGram(M): # 행렬의 QR 분해
    
    col = len(M)
    row = len(M[0])

    transM = transpose(M)
    U = []                          # 직교 벡터 u의 집합
    normList = []                   # 직교 벡터 u의 길이 집합

    V = []                          # 정규 직교 벡터 v의 집합
    Q = []                          # Q 행렬
    R = []                          # R 행렬

    