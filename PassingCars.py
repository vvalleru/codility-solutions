def solution(A):
    result = 0
    east_cars = 0
    
    for i in A:
        if i == 1:
            result += east_cars
            if result > 1000000000:
                return -1
        else:
            east_cars += 1
    
    return result