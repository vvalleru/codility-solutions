def solution(A):
    result = 0
    for i in xrange(len(A)):
        result ^= A[i]
        result ^= (i + 1)
    
    return result ^ (len(A) + 1)