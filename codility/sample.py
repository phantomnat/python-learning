def solution(N, M, X, Y):
    # write your code in Python 3.6

    max_goldmine = len(X)
    ways = 0
    
    if max_goldmine % 2 == 1:
        return ways
        
    x_goldmine = {}
    y_goldmine = {}
    
    for xg in X:
        if xg not in x_goldmine:
            x_goldmine[xg] = 0
        x_goldmine[xg] += 1
    for yg in Y:
        if yg not in y_goldmine:
            y_goldmine[yg] = 0
        y_goldmine[yg] += 1
    
    # print(x_goldmine)
    # print(y_goldmine)
    
    lx_sum, rx_sum = 0, 0
    ly_sum, ry_sum = 0, 0
    lx, rx = 0, N
    ly, ry = 0, M
    
    while rx >= lx or ry >= ly:
        if rx >= lx:
            if lx_sum == rx_sum == max_goldmine // 2:
                ways += 1
                lx += 1
            elif lx_sum <= rx_sum:
                lx_sum += x_goldmine.setdefault(lx, 0)
                lx += 1
            else:
                rx_sum += x_goldmine.setdefault(rx-1, 0)
                rx -= 1

        if ry >= ly:
            if ly_sum == ry_sum == max_goldmine // 2:
                ways += 1
                ly += 1
            elif ly_sum <= ry_sum:
                ly_sum += y_goldmine.setdefault(ly, 0)
                ly += 1
            else:
                ry_sum += y_goldmine.setdefault(ry-1, 0)
                ry -= 1
            
    return ways

# print(solution(5,5, [0,4,2,0], [0,0,1,4]))
print(solution(5,5, [0,4], [0,0]))