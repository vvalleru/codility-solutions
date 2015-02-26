def solution(A):
    A.sort()
    # check for the  lowest numbers, if negative
    return max(A[-1] * A[0] * A[1], A[-1] * A[-2] * A[-3])