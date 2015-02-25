def solution(A):
    N = len(A)
    # The missing positive integer should be with in the range 1 to N
    flags = [False] * N
    
    for i in A:
        if 0 < i <= N:
            flags[i - 1] = True


    for i in xrange(len(flags)):
        if not flags[i]:
            return i + 1

    return len(flags) + 1