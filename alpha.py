def solution(A):
    N = len(A)
    counters = [0] * N
    
    for number in A:
        counters[number] += 1
    
    for index in xrange(N - 1, -1, -1):
        counters[A[index]] -= 1
        if counters[A[index]] == 0:
            return index
    return -1