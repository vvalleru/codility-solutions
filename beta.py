def solution(A):
    front_edges = []
    back_edges = []
    result = 0
    front_index = 0
    back_index = 0

    for index in xrange(len(A)):
        # record the front edges and back edges for each disc
        front_edges.append(index + A[index])
        back_edges.append(index - A[index])

    front_edges.sort()
    back_edges.sort()

    while front_index < len(A):
        while back_index < len(A) and\
            back_edges[back_index] <= front_edges[front_index]:
            back_index += 1
        # for each front edge look at the num of back edges before it (this
        #   means all the back edges are intersections of the front edge),
        # finally, -1 for the current disc's back edge
        result += back_index - front_index - 1
        if result > 10000000:
            return -1
        front_index += 1

    return result