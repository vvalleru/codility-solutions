def solution(S):
    open = 0
    
    for bracket in S:
        if bracket == "(":
            open += 1
        else:
            if open < 1:
                return 0
            else:
                open -= 1
    if open == 0:
        return 1
    
    return 0