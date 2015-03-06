def solution(N):
    i = 1
    length = i
    while i * i <= N:
        if N % i == 0:
            length = i
        i += 1
    
    breadth = N // length
    
    return 2 * (length + breadth)