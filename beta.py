def solution(A):
    frontEdges = []
    backEdges = []
    result = 0
    front_index = 0
    back_index = 0

    for index in xrange(len(A)):
        # record the front edges and back edges for each disc
        frontEdges.append(index + A[index])
        backEdges.append(index - A[index])

    frontEdges.sort()
    backEdges.sort()

    while front_index < len(A):
        while back_index < len(A) and\
            backEdges[back_index] <= frontEdges[front_index]:
            back_index += 1
        # for each front edge look at the num of back edges before it (this
        #   means all the back edges are intersections of the front edge),
        # finally, -1 for the current disc's back edge
        result += back_index - front_index - 1
        if result > 10000000:
            return -1
        front_index += 1

    return result