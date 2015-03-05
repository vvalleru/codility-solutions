def solution(A):
    size = 0
    value = 0
    
    for element in A:
        if size > 0 and value == element:
            size += 1
        elif size > 0 and value != element:
            size -= 1
        else:
            value = element
            size += 1
    
    count = 0
    result = -1
    
    if size > 0:
        for index in xrange(len(A)):
            if A[index] == value:
                result = index 
                count += 1
    
    if count > len(A) // 2:
        return result

    return -1