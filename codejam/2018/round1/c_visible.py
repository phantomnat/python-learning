import math
t = int(input())

for i in range(1, t+1):
    # ans = 0
    n, p = [int(s) for s in input().split()]
    cookies = []
    # cookie_w =
    begin_p = 0
    max_p = 0
    cutted_p = 0
    for _ in range(n):
        w, h = [float(s) for s in input().split()]
        begin_p += 2 * (w + h)
        max_p += 2 * (math.sqrt((w**2) + (h**2)) + w + h)
        cookies.append({'w': w, 'h': h})
    # print(cookies)
    if begin_p == p:
        cutted_p = begin_p
    else:
        cutted_p = p if max_p >= p else max_p

    print('Case #{}: {:.6f}'.format(i, float(cutted_p)))