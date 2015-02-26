def solution(A):
    A_len = len(A)
    result = 0
    A.sort()
    
    for index in xrange(A_len):
        if A[index] == A[(index + 1) % A_len]:
            # % A_len to deal with out of bounds
            continue
        result += 1
    
    if A_len > 0 and A[0] == A[-1]:
        # if all the elements in the array are same
        result += 1
        
    return result