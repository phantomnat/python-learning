T = int(input())

for _ in range(T):
    str1_n, str2_n = [int(s) for s in input().split()]
    str1 = input()
    str2 = input()
    
    cache = {}
        
    def lcs(str1, str1_n, str2, str2_n):
        key = '%s_%s' % (str1_n,str2_n)
        if key in cache:
            return cache[key]
        if str1_n <= 0 or str2_n <= 0:
            return 0
        # print('%s %s' % (str1, str2))
        if str1[-1] == str2[-1]:
            count = 1 + lcs(str1[:str1_n-1], str1_n-1, str2[:str2_n-1], str2_n-1)
        else:
            count = max(
                lcs(str1[:str1_n-1], str1_n-1, str2[:str2_n], str2_n),
                lcs(str1[:str1_n], str1_n, str2[:str2_n-1], str2_n-1)
            )
        cache[key] = count
 
        return count
                    
    
    
    ans = lcs(str1, str1_n, str2, str2_n)
    # print(cache)
    print(ans)
