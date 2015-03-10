from math import sqrt

def solution(A):
    N = len(A)
    if N < 3:
        return 0
    
    (totalFlags, nextFlagIndices) = getTotalFlagsAndNextFlagIndices(A)
    maxFlags = min(int(totalFlags), int(sqrt(N)) + 1)

    if totalFlags < 2:
        return totalFlags
    
    for flags in xrange(maxFlags, 0, -1):
        if canNFlagsBePlanted(flags, nextFlagIndices):
            return flags
    return 0

def getTotalFlagsAndNextFlagIndices(A):
    N = len(A)
    totalFlags = 0
    nextFlagIndices = [-1] * N
    
    for index in xrange(N - 2, 0 , -1):
        nextFlagIndices[index] = nextFlagIndices[index + 1]
        if A[index - 1] < A[index] > A[index + 1]:
            totalFlags += 1
            nextFlagIndices[index] = index
    nextFlagIndices[0] = nextFlagIndices[1]
    
    return (totalFlags, nextFlagIndices)

def canNFlagsBePlanted(k, nextFlagIndices):
    N = len(nextFlagIndices)
    K = k
    remainingFlags = K
    currentFlagPosition = nextFlagIndices[0]

    while -1 < nextFlagIndices[currentFlagPosition] < N and remainingFlags > 0:
        remainingFlags -= 1
        if currentFlagPosition + K > N - 1:
            break
        currentFlagPosition = nextFlagIndices[currentFlagPosition + K]

    if remainingFlags == 0:
            return True
    return False