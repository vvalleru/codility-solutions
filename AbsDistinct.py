def solution(A):
    result = 0
    non_dups = [0] * len(A)
    end = 0
    non_dups[0] = A[0]
    
    for element in A:
        if non_dups[end] != element:
            end += 1
            non_dups[end] = element
        
    start = 0
    while start <= end:
        if abs(non_dups[start]) > abs(non_dups[end]):
            start += 1
        elif abs(non_dups[start]) < abs(non_dups[end]):
            end -= 1
        else:
            start += 1
            end -= 1
        result += 1
        
    return result