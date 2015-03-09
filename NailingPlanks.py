def check(A, B, C, K):
    # sort the nails if the positions are random
    C.sort()
    C_len = len(C)
    A_len = len(A)
    i = 0 
    j = 0

    while K > 0 and i < C_len:
        while j < A_len:
            if A[j] <= C[i] <= B[j]:
                j += 1
            else:
                break
        K -= 1
        i += 1

    if K < 0 or j < A_len:
        return False
    else:
        return True

def solution(A, B, C):
    # sort the lists if random
    A, B = (list(x) for x in zip(*sorted(zip(A, B), key=lambda pair: pair[0])))

    # use binary search to findout the minimum number of nails needed
    minPlanks = 1
    maxPlanks = len(C)
    result = -1

    while minPlanks <= maxPlanks:
        currMax = (minPlanks + maxPlanks) / 2

        # pass in only the first currMax num of nails to check
        if check(A, B, C[:currMax], currMax):
            maxPlanks = currMax - 1
            result = currMax
        else:
            minPlanks = currMax + 1

    return result