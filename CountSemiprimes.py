def solution(N, P, Q):
    factorizedArray = getFactorizedArray(N)
    semiPrimesTillHere = [0] * (N + 1)
    result = [0] * len(P)
    
    for index in xrange(2, N + 1):
        semiPrimesTillHere[index] = semiPrimesTillHere[index - 1]
        if isSemiPrime(factorizedArray, index):
            semiPrimesTillHere[index] += 1

    for index in xrange(len(result)):
        result[index] = semiPrimesTillHere[Q[index]] - semiPrimesTillHere[P[index] - 1]
    return result
    
    
def getFactorizedArray(N):
    factorizationArray = [0] * (N + 1)
    
    for each in xrange(2, N + 1):
        index = each + each
        while index < N + 1:
            if factorizationArray[index] == 0:
                factorizationArray[index] = each
            index += each
    return factorizationArray
    
def isSemiPrime(factorizedArray, N):
    if factorizedArray[N] != 0 and\
    N / factorizedArray[N] != 0 and\
    factorizedArray[N / factorizedArray[N]] == 0:
        return True
    return False