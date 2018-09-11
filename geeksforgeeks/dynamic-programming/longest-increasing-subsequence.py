# https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [int(s) for s in input().split()]
    cache = {}
    
    def lis(arr, n, val):
        if n <= 0:
            return 0
        if n in cache:
            return cache[n]
        # print(arr)
        count = 0
        for i,v in enumerate(arr):
            if v > val:
                count = max(count, 1 + lis(arr[i+1:], n-i-1, v))
        cache[n] = count
        return count

    ans = 0
    for i,v in enumerate(arr):
        ans = max(ans, 1+lis(arr[i+1:], N-i-1, v))
    
    print(ans)
    # print(cache)