def solution(S):
    stack = [0] * len(S)
    top = -1
    
    for bracket in S:
        if bracket == "{" or\
            bracket == "[" or\
            bracket == "(":
                top += 1
                stack[top] = bracket
        else:
            if top > -1 and (bracket == "}" and stack[top] == "{") or\
                            (bracket == "]" and stack[top] == "[") or\
                            (bracket == ")" and stack[top] == "("):
                # pop the stack
                top -= 1
            else:
                return 0

    if top == -1:
        return 1

    return 0