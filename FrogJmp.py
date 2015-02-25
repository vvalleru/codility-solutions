def solution(X, Y, D):
    # Jump from position zero to Y
    Y -= X
    result = Y / D

    # Needs an extra jump to cover the remainder distance
    if Y % D != 0:
        return result + 1
    
    return result