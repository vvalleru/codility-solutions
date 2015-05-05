def solution(finalPosition, leaves):
  positionsOnTheRiver = [False] * (finalPosition + 1)
    
  for currentLeaf in xrange(len(leaves)):
    if not positionsOnTheRiver[leaves[currentLeaf]]:
      # if there is no leaf at the current position,
      # mark the position and decrement the count of positions to be covered
      positionsOnTheRiver[leaves[currentLeaf]] = True
      finalPosition -= 1

    if finalPosition == 0:
      return currentLeaf
  return -1