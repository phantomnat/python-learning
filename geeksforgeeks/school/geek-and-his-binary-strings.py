# https://practice.geeksforgeeks.org/problems/geek-and-his-binary-strings/0
# Dynamic-Programming
def genkey(x, y):
    if x == y:
        return str(x)
    return '{}{}'.format(x,y)

def calc(bstr):
    for i in range(2, 1001):
        for j in range(i):
            bstr[i] += bstr[j]*bstr[i-j-1]
            bstr[i] %= 1000000007
    # if genkey(ONEs, ZEROs) in bstr_map:
    #     return bstr_map[genkey(ONEs, ZEROs)]
    # for zero in range(1, ZEROs+1):
    #     bstr_map[genkey(0, zero)] = 1
    # for one in range(1, ONEs+1):
    #     for zero in range(ZEROs+1):
    #         s = bstr_map[genkey(one-1, zero)]
    #         if zero > one:
    #             s += bstr_map[genkey(one, zero-1)]
    #         bstr_map[genkey(one,zero)] = s % 1000000007

    # return bstr_map[genkey(ONEs, ZEROs)]

# # bstr_map = {(1,1): 1}
# N = 1000
# ans = solve2(N, N, {})
# # print(ans)
# bstr_map = {genkey(0,0):0}
# assert solve(8, 8, bstr_map) == 1430
bstr = [0] * 1000
bstr[0] = bstr[1] = 1
calc(bstr)

T = int(input())

for _ in range(T):
    N = int(input())
    ans = bstr[N]
    print(ans)
