def solution(N, A):
    max_counters = 0
    curr_max = 0
    counters = [0] * N
    
    for each in A:
        if each < N + 1:
            if max_counters > counters[each - 1]:
                counters[each - 1] = max_counters
            counters[each - 1] += 1
            curr_max = max(curr_max, counters[each - 1])
        else:
            max_counters = curr_max

    for index in xrange(len(counters)):
        if counters[index] < max_counters:
            counters[index] = max_counters
    
    return counters