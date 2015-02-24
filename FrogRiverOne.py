def solution(X, A):
    flags = [0] * (X + 1)
    
    for i in xrange(len(A)):
        if flags[A[i]] == 0:
            flags[A[i]] = 1
            X -= 1
        if X == 0:
            return i
    return -1