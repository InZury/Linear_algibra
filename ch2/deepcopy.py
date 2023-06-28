from zero_mat import zero_mat

def deepcopy(arr):
    # 깊은 복사 구현
    # mutable 객체 복사에 사용
    
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