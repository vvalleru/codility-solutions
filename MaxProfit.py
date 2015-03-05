def solution(A):
    max_profit = 0
    curr_profit = 0
    curr_sell_price = 0
    
    for day in xrange(len(A) - 1, -1 , -1):
        curr_sell_price = max(curr_sell_price, A[day])
        curr_profit = max(curr_profit, curr_sell_price - A[day])
        max_profit = max(max_profit, curr_profit)
    
    return max_profit