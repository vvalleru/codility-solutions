def solution(A):
    N = len(A)
    result = [0] * N
    divisors = countDivisors(A)
    
    for index in xrange(N):
        result[index] = N - divisors[A[index]]
    
    return result

def countDivisors(A):
    A_max = max(A)
    divisors = [0] * (A_max + 1)
    
    for element in A:
        i = element
        while i < (A_max + 1):
            divisors[i] += 1
            i += element
    return divisors

print solution([1,2,3,4,5,6,7,8,9,10])