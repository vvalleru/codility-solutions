def solution(A, B):
    upstream = [0] * len(A)
    top = -1
    fishes_alive = 0
    
    for fish_position in xrange(len(A)):
        if B[fish_position] == 1:
            top += 1
            upstream[top] = A[fish_position]
        else:
            while top > -1 and A[fish_position] > upstream[top]:
                top -= 1
            if top == -1:
                if B[fish_position] == 0:
                    fishes_alive += 1
                else:
                    top += 1
                    upstream[top] = A[fish_position]
    fishes_alive += (top + 1)
    return fishes_alive