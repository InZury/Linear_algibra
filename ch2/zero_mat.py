def zero_mat(col, row):
    # 영 행렬 생성
    
    zero = []
    
    for i in range(col):
        sub = []
        for j in range(row):
            sub.append(0)
        zero.append(sub)
    
    return zero