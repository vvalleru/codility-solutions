def solution(S, P, Q):
    # a table to record the last occurrences of the indexes
    table = [[-1] * len(S) for i in range(4)]
    result = [0] * len(Q)
    
    for index in xrange(len(S) - 1, -1, -1):
        # record the indexes in the reverse order
        table[0][index] = table[0][(index + 1) % len(S)]
        table[1][index] = table[1][(index + 1) % len(S)]
        table[2][index] = table[2][(index + 1) % len(S)]
        table[3][index] = table[3][(index + 1) % len(S)]
        
        if S[index] == 'A':
            table[0][index] = index
        elif S[index] == 'C':
            table[1][index] = index
        elif S[index] == 'G':
            table[2][index] = index
        else:
            table[3][index] = index
    
    for query in xrange(len(P)):
        # check from the minimum possible value, if it occurs within the range
        if P[query] <= table[0][P[query]] <= Q[query]:
            result[query] = 1
        elif P[query] <= table[1][P[query]] <= Q[query]:
            result[query] = 2
        elif P[query] <= table[2][P[query]] <= Q[query]:
            result[query] = 3
        else:
            result[query] = 4
    
    return result