# 가우스 조르단 소거법을 이용한 선형 시스템의 해 계산

def zero_mat(col, row): # 영 행렬
    
    zero = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(0)
        zero.append(sub)
        
    return zero

def deepcopy(arr): # 깊은 복사 구현
    
    if type(arr[0]) == list:
        col = len(arr)
        row = len(arr[0])
        result = zero_mat(col, row)
     
        for i in range(col):
            for j in range(row):
                result[i][j] = arr[i][j]
        
        return result
    else:
        row = len(arr)
        result = []
        
        for i in range(row):
            result.append(arr[i])
            
        return result
    
def gje(M, u): # 가우스 조르단 소거법
    
    gaussM = deepcopy(M)
    gaussV = deepcopy(u)
    col = len(gaussM)
    row = col
    
    for i in range(col):
        xRow = gaussM[i]
        yVal = gaussV[i]
        
        if xRow[i]:
            temp = 1 / xRow[i]
        else:
            temp = 0
            
        xRow = [element * temp for element in xRow]
        yVal *= temp
        
        gaussM[i] = xRow
        gaussV[i] = yVal
        
        for j in range(row):
            if i == j:
                continue
            
            xNext = gaussM[j]
            yNext = gaussV[j]
            xTemp = [element * -xNext[i] for element in xRow]
            yTemp = yVal * (-xNext[i])
            
            for k in range(len(xRow)):
                xNext[k] = xTemp[k] + xNext[k]
            yNext = yTemp + yNext
            
            gaussM[j] = xNext
            gaussV[j] = yNext
            
    return gaussV