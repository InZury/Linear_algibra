# 벡터의 연산을 u, v의 벡터 계산

def v_sum(u, v):
    # 벡터의 덧셈
    
    row = len(u)
    result = []
    
    for i in range(row):
        result.append(u[i] + v[i])
        
    return result

def v_sub(u, v):
    # 벡터의 뺄셈
    
    row = len(u)
    result = []
    
    for i in range(row):
        result.append(u[i] - v[i])
        
    return result

def v_scala_mul(scala, u):
    # 벡터의 스칼라 곱
    
    row = len(u)
    result = []
    
    for i in range(row):
        result.append(scala * u[i])
        
    return result

def v_mul(u, v):
    # 벡터의 원소 곱
    
    row = len(u)
    result = []
    
    for i in range(row):
        result.append(u[i] * v[i])
        
    return result

def v_div(u, v):
    # 벡터의 나눗셈
    
    row = len(u)
    result = []
    
    for i in range(row):
        result.append(u[i] / v[i])
        
    return result