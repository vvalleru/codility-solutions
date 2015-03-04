def solution(H):
    stack = [0] * len(H)
    top = -1
    stones = 0
    
    for building in H:
        if top > -1 and stack[top] < building:
            top += 1
            stack[top] = building
        else:
            while top > -1 and stack[top] > building:
                top -= 1
                stones += 1
            if top == -1 or (top > -1 and stack[top] < building):
                top += 1
                stack[top] = building
    stones += (top + 1)
    
    return stones