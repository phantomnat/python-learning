# https://practice.geeksforgeeks.org/problems/row-with-minimum-number-of-1s/0

T = int(input())

for _ in range(T):
    Y, X = [int(s) for s in input().split()]
    array = [int(s) for s in input().split()]
    ans = -1
    row_count = [0] * Y
    is_done = False
    for x in range(X-1, -1, -1):
        for y in range(Y):
            oned_pos = (X*y)+x
            if x < X-1 and row_count[y] > 0 and array[oned_pos] == 0:
                ans = y
                is_done = True
                break

            if array[oned_pos] == 1:
                row_count[y] += 1
                if ans == -1: ans = y
            # el
            # row_count[y] += 1 if array[oned_pos] == 1 else 0

        if (x == X-1 and sum(row_count) == 0) or is_done:
            break
    print(ans)
