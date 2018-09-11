# https://practice.geeksforgeeks.org/problems/equal-to-product/0

T = int(input())

for _ in range(T):
    N, P = [int(s) for s in input().split()]
    array = [int(s) for s in input().split()]

    target_multiply = {}
    ans = 'No'
    for _, a in enumerate(array):
        if float(a) in target_multiply:
            ans = 'Yes'
            break
        target = float(P) / a if a > 0 else 0
        target_multiply[target] = 1
    
    print(ans)

'''
2
5 2
1 2 3 4 5
8 46
5 7 9 22 15 344 92 8
'''