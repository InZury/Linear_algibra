# 하우스홀더 행렬 구현

def outer_product(u, v): # 외적
    
    rowU = len(u)
    rowV = len(v)
    result = []
    
    for i in range(rowU):
        sub = []
        for j in range(rowV):
            val = u[i]*v[j]
            sub.append(val)
        result.append(sub)
        
    return result
    
def inner_product(u, v): # 내적
    
    rowU = len(u)
    result = 0
    
    for i in range(rowU):
        result += u[i]*v[i]
    
    return result

def m_identity(n): # 단위 행렬
    
    result = []
    
    for i in range(n):
        sub = []
        for j in range(n):
            if(i == j):
                sub.append(1)
            else:
                sub.append(0)
        result.append(sub)
        
    return result

def m_sub(M, N): # 행렬의 뺄셈
    
    col = len(M)
    row = len(M[0])
    result = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(M[i][j] - N[i][j])
        result.append(sub)
        
    return result

def m_householder(M): # 하우스홀더 행렬
    
    col = len(M)
    oM = outer_product(M, M)
    iM = inner_product(M, M)
    result = []
    
    for i in range(col):
        sub = []
        for j in range(col):
            val = (2 / iM) * oM[i][j]
            sub.append(val)
        result.append(sub)
        
    house = m_sub(m_identity(col), result)
    
    return house