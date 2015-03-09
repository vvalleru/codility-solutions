def solution(A):
    A.sort()
    result = 0
    for x in xrange(len(A)):
        z = 0
        for y in xrange(x + 1, len(A)):
            while z < len(A) and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result