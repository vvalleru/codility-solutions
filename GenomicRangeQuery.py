def solution(S, P, Q):    
    nextOccurrencePositions = recordNextOccurrencePosition(S)
    return getQueryResults(P, Q, nextOccurrencePositions)

def recordNextOccurrencePosition(S):
    # a table to record the last occurrences of the indexes
    nextOccurrencePositions = [[-1] * len(S) for i in range(4)]

    for index in xrange(len(S) - 1, -1, -1):
        # record the next occurrence position
        nextOccurrencePositions[0][index] = nextOccurrencePositions[0][(index + 1) % len(S)]
        nextOccurrencePositions[1][index] = nextOccurrencePositions[1][(index + 1) % len(S)]
        nextOccurrencePositions[2][index] = nextOccurrencePositions[2][(index + 1) % len(S)]
        nextOccurrencePositions[3][index] = nextOccurrencePositions[3][(index + 1) % len(S)]
        
        if S[index] == 'A':
            nextOccurrencePositions[0][index] = index
        elif S[index] == 'C':
            nextOccurrencePositions[1][index] = index
        elif S[index] == 'G':
            nextOccurrencePositions[2][index] = index
        else:
            nextOccurrencePositions[3][index] = index
    
    return nextOccurrencePositions

def getQueryResults(begin, end, nextOccurrences):
    # to store the results of all the queries
    answers = [0] * len(begin)

    for query in xrange(len(begin)):
        # check from the minimum possible value, if it occurs within the range inclusive
        if begin[query] <= nextOccurrences[0][begin[query]] <= end[query]:
            answers[query] = 1
        elif begin[query] <= nextOccurrences[1][begin[query]] <= end[query]:
            answers[query] = 2
        elif begin[query] <= nextOccurrences[2][begin[query]] <= end[query]:
            answers[query] = 3
        else:
            answers[query] = 4
    
    return answers