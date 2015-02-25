def solution(X, A):
    flags = [False] * (X + 1)
    
    for i in xrange(len(A)):
        if not flags[A[i]]:
            # if there is no leaf at the current position,
            # mark the position and decrement the count of positions to be covered
            flags[A[i]] = True
            X -= 1

        if X == 0:
            return i
    return -1