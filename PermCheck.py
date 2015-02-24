def solution(A):
    N = len(A)
    lookup = [0] * (N + 1)
    
    for i in A:
        if i > N :
            return 0
        lookup[i] += 1
        
    for i in xrange(1, N + 1):
        if lookup[i] != 1:
            return 0
    return 1