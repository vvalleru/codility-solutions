def solution(A):
    left_sum = A[0]
    right_sum = sum(A) - left_sum
    
    result = abs(left_sum - right_sum)
    
    for index in xrange(1, len(A) - 1):
        left_sum += A[index]
        right_sum -= A[index]
        
        result = min(result, abs(left_sum - right_sum))
    
    return result