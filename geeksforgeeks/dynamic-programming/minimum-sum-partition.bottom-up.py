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

    # Create an array to store results of subproblems
    dp = [[0 for _ in range(total+1)] for _ in range(N+1)]

    # Initialize first column as true. 0 sum is possible  
    # with all elements. 
    for i in range(N+1):
        dp[i][0] = 1

    # Initialize top row, except dp[0][0], as false. With 
    # 0 elements, no other sum except 0 is possible 
    for i in range(1,total+1):
        dp[0][i] = 0

    # Fill the partition table in bottom up manner 
    for i in range(1,N+1):
        for j in range(1,total+1):
            dp[i][j] = dp[i-1][j]

            if arr[i-1] <= j:
                dp[i][j] |= dp[i-1][j-arr[i-1]]

    for i in range(N+1):
        print(dp[i])