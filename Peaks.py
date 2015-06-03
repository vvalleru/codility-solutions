def solution(A):
    N = len(A)
    
    if N < 3:
        return 0
        
    peaks_till_here = get_peaks_till_here(A)
    
    for k in range(2, N + 1):
        if N % k == 0 and check_partition(k, peaks_till_here):
            return N / k
    return 0
    
def get_peaks_till_here(A):
    peaks_till_here = [0] * len(A)
    
    for i in xrange(1, len(A) - 1):
        peaks_till_here[i] = peaks_till_here[i - 1]
        
        if A[i - 1] < A[i] > A[i + 1]:
            peaks_till_here[i] += 1
    
    peaks_till_here[-1] = peaks_till_here[-2]
    
    return peaks_till_here
    
def check_partition(k, peaks_till_here):
    i = len(peaks_till_here) - 1
    
    while i - k >= 0:
        if peaks_till_here[i] <= peaks_till_here[i - k]:
            return False
        i -= k
        
    if peaks_till_here[k - 1] < 1:
        return False
    return True