def solution(A):
    A_len = len(A)
    A.sort()
    
    if A_len < 3:
        # if there are no enough elements to form a triangle
        return 0
        
    for index in xrange(A_len):
        # % A_len, to deal with the overflow
        first_side = A[index]
        second_side = A[(index + 1) % A_len]
        third_side = A[(index + 2) % A_len]
        
        if first_side + second_side > third_side and\
        first_side + third_side > second_side and\
        second_side + third_side > first_side:
            return 1
    
    return 0