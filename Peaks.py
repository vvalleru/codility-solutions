def solution(A):
    N = len(A)
    peaks_till_here = [0] * N
    
    if N < 3:
        return 0
    
    for index in xrange(1, N - 1):
        peaks_till_here[index] = peaks_till_here[index - 1] 
        if A[index - 1] < A[index] > A[index + 1]:
            peaks_till_here[index] += 1
    peaks_till_here[-1] = peaks_till_here[N - 2]
    
    i = 1
    while i <= N:
        if N % i == 0 and check(peaks_till_here, i):
            return N / i
        i += 1
    return 0
    
def check(peaks_till_here, block_size):
    N = len(peaks_till_here)
    previous_peaks = 0
    i = block_size - 1
    while i < N:
        if peaks_till_here[i] == previous_peaks:
            return False
        previous_peaks = peaks_till_here[i]
        i += block_size
    return True