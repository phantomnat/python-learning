# https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
'''
Input:
2
4
1 6 5 11
4
36 7 46 40

10
1 7 46 40 13 9 43 5 2 22

Output: 
1
23
'''

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [int(s) for s in input().split()]
    total = sum(arr)
    cache = {}
    # sol = {}
    # dp = [[0 for _ in range(total+1)] for _ in range(N+1)]
    # for i in range(N+1):
    #     dp[i][0] = 1
    # for i in range(1,total+1):
    #     dp[0][i] = 0
    # for i in range(1,N+1):
    #     for j in range(1,total+1):
    #         dp[i][j] = dp[i-1][j]
    #         if arr[i-i] < j:
    #             dp[i][j] |= dp[i-1][j-arr[i-1]]

    # call_cnt = {'c':0}
    def minsum(arr, N, total, calculated):
        # _t = sum(calculated)
        # call_cnt['c'] += 1
        if N < 0:
            diff = abs((total-calculated) - calculated)
            # print('%s  (%d)' % (calculated, diff))

            return diff
        # if N in cache:
        #     return cache[N]
        key='%s_%s' %(N, calculated)
        if key in cache:
            return cache[key]
        # count = float('inf')
        # for i,v in enumerate(arr):
        #     count = min(
        #         count,
                
        #         minsum(arr[:i]+arr[i+1:], N-1, total, set1)
        #     )
        # diff = 
        s1=minsum(arr, N-1, total, calculated+arr[N])
        s0=minsum(arr, N-1, total, calculated)
        if s1 < s0:
            cache[key] = s1
            # sol[key] = calculated+[arr[N]]
        else:
            cache[key] = s0
            # sol[key] = calculated
        # cache[key] = min(
        #     minsum(arr, N-1, total, calculated+[arr[N]]),
        #     minsum(arr, N-1, total, calculated)
        # )
        # if N == 9:
        #     print()
        return cache[key]
    
    ans = minsum(arr, N-1, total, 0)

    # print('total %d' % total)
    print(ans)
    # print(cache)
    # print(sol['%s_%s' % (N-1, 0)])
    # print(call_cnt)
    # print(dp)
    # for i in range(N+1):
    #     print(dp[i])