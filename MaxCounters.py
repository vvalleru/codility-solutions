def solution(N, A):
    max_counter = 0
    curr_max = 0
    counters = [0] * N
    
    for each in A:
        # increment(X) operation
        if each < N + 1:
            # catchup the lagging value
            if max_counter > counters[each - 1]:
                counters[each - 1] = max_counter
            # increment the value
            counters[each - 1] += 1
            # record the current value
            curr_max = max(curr_max, counters[each - 1])
        else:
            # max counters operation, record the new value
            max_counter = curr_max

    # catchup the lagging values for the remaining operations
    for index in xrange(len(counters)):
        if counters[index] < max_counter:
            counters[index] = max_counter
    
    return counters