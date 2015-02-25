def solution(A, K):
    prev_row = [0] * len(A[0])
    prev_row[0] = K

    for row_index in xrange(len(A)):
        # first switch in each row doesn't have any balls coming from right
        balls_going_right = 0
        for col_index in xrange(len(A[0])):
            total_balls = balls_going_right + prev_row[col_index]
            if A[row_index][col_index] == -1:
                # one extra ball down for odd input
                balls_going_right = total_balls / 2
                prev_row[col_index] = total_balls - balls_going_right
            elif A[row_index][col_index] == 1:
                # one extra ball to the right for odd input
                prev_row[col_index] = total_balls / 2
                balls_going_right = total_balls - prev_row[col_index]
            # the direction of the balls doesn't change for a zero switch
    return prev_row[-1]