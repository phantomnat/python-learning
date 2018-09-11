# https://practice.geeksforgeeks.org/problems/edit-distance/0

T = int(input())

for _ in range(T):
    str1_n, str2_n = [int(s) for s in input().split()]
    str1, str2 = [s for s in input().split()]

    cache = {}

    def distance(str1, str1_n, str2, str2_n):
        key = '%s_%s' % (str1_n, str2_n)
        # print('%s %s' % (str1, str2))
        if key in cache:
            return cache[key]

        count = 0

        if str1_n <= 0 and str2_n <= 0:
            return 0
        elif str1_n <= 0 or str2_n <= 0:
            return max(str1_n, str2_n)

        if str1[-1] == str2[-1]:
            count = distance(str1[:str1_n-1], str1_n-1, str2[:str2_n-1], str2_n-1)
        else:
            count = min(
                # remove
                1 + distance(str1[:str1_n-1], str1_n-1, str2[:str2_n], str2_n),    
                1 + distance(str1[:str1_n], str1_n, str2[:str2_n-1], str2_n-1),
                # add
                # 1 + distance(str1[:str1_n], str1_n, str2[:str2_n-1], str2_n-1),
                # 1 + distance(str1[:str1_n], str1_n, str2[:str2_n-1], str2_n-1),
                # replace
                1 + distance(str1[:str1_n-1], str1_n-1, str2[:str2_n-1], str2_n-1)
            )
        cache[key] = count
        return count

    count = distance(str1, str1_n, str2, str2_n)
    print(count)
    # print(cache)

