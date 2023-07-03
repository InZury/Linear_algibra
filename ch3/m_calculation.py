# 행렬의 연산을 M, N의 행렬 계산

def m_sum(M, N):
    # 행렬의 덧셈
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(M[i][j] + N[i][j])
        result.append(sub)
    
    return result

def m_sub(M, N):
    # 행렬의 뺄셈
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(M[i][j] - N[i][j])
        result.append(sub)
        
    return result

def m_scala_mul(scala, M):
    # 행렬의 스칼라 곱
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(scala * M[i][j])
        result.append(sub)
        
    return result

def m_element_mul(M, N):
    # 행렬의 원소 곱
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(M[i][j] * N[i][j])
        result.append(sub)
        
    return result

def m_mul(M, N):
    # 행렬의 행렬 곱
    
    col = len(M)
    row = len(M[0])
    subRow = len(N[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(subRow):
            val = 0
            for k in range(row):
                val += M[i][k] * N[k][j]
            sub.append(val)
        result.append(sub)
    
    return result