def solution(X, Y, D):
    Y -= X
    result = Y / D
    
    if Y % D != 0:
        return result + 1
    
    return result