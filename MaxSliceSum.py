def solution(A):
    max_slice = 0
    curr_max = 0
    slice = [0] * len(A)

    for index in xrange(len(A)):
        curr_max = max(0, curr_max + A[index])
        max_slice = max(max_slice, curr_max)
        slice[index] = max_slice

    for each in slice:
        if each != 0:
            return max_slice

    return max(A)