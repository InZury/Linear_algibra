# n X n 행렬식 계산

def zero_mat(col, row): # 영 행렬
    
    zero = []

    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(0)
        zero.append(sub)
    
    return zero

def deepcopy(arr): # 깊은 복사

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
    
def det_rec(M): # 행렬식 계산

    col = len(M)
    result = 0

    if col == 2: # 2x2 행렬의 행렬식
        result = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return result
    
    for i in range(col): # nxn 행렬의 행렬식
        X = deepcopy(M)
        X = X[1:]
        colX = len(X)

        for j in range(colX):
            X[j] = X[j][0:i] + X[j][i+1:]

        cof = (-1) ** (i % 2) # 여인수 계산

        sub_det = det_rec(X)
        result += cof * M[0][i] * sub_det
    
    return result

def det_tri(M): # 상 삼각 행렬 변환으로 행렬식 계산

    col = len(M)
    X = deepcopy(M)
    changedRow = 0

    for i in range(col):
        if X[i][i] == 0:
            temp = X[i+1]
            X[i+1] = X[i]
            X[i] = temp
            changedRow += 1
        
        for j in range(i+1, col):
            ratio = X[j][i] / X[i][i]
            for k in range(col):
                X[j][k] = X[j][k] - ratio * X[i][k]
    
    changedRow = -1 ** changedRow
    result = 1

    for i in range(col):
        result *= X[i][i]

    result = changedRow

    return result