# 다양한 행렬의 형태를 M 행렬을 이용하여 표현

def m_transpose(M): # 전치 행렬
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(row):
        sub = []
        for j in range(col):
            sub.append(M[j][i])
        result.append(sub)
        
    return result

def m_diag(M): # 대각 행렬
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            if i == j:
                sub.append(M[i][j])
            else:
                sub.append(0)
        result.append(sub)
        
    return result

def m_diag_element(M): #대각 행렬의 원소
    
    row = len(M)
    result = []
    
    for i in range(row):
        result.append(M[i][i])
        
    return result

def e_diag(m): # 대각 행렬 원소로 대각 행렬 생성   
    
    row = len(m)
    result = []
    
    for i in range(row):
        sub = []
        for j in range(row):
            if i == j:
                sub.append(m[i])
            else:
                sub.append(0)
        result.append(sub)
        
    return result

def m_identity(n): # n 크기 단위 행렬 생성
    
    result = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
        
    return result

def m_utri(M): # 상 삼각 행렬
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            if i > j:
                sub.append(0)
            else:
                sub.append(M[i][j])
        result.append(sub)
        
    return result

def m_ltri(M): # 하 삼각 행렬
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            if i < j:
                sub.append(0)
            else:
                sub.append(M[i][j])
        result.append(sub)
        
    return result

def m_toeplitz(M, N): # 토플리츠 행렬
    
    col = len(M)
    row = len(N)
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            if i > j:
                sub.append(M[i - j])
            else:
                sub.append(N[j - i])
        result.append(sub)
    
    return result

def m_upper_bidiag(M): # 상 이중 대각 행렬 (upper_bidiagonal)
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            if i > j or j - i > 1:
                sub.append(0)
            else:
                sub.append(M[i][j])
        result.append(sub)
        
    return result

def m_lower_bidiag(M): # 하 이중 대각 행렬 (lower_bidiagonal)
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            if i < j or i - j > 1:
                sub.append(0)
            else:
                sub.append(M[i][j])
        result.append(sub)
        
    return result