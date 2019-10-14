from typing import List
from collections import defaultdict

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        total = sum(cost)
        if maxCost >= total:
            return n
        elif n == 0:
            return 0
        ans = 0
        l, r = 0, 0
        currentCost = 0
        while r < n:
            c = cost[r]
            currentCost += c
            if currentCost <= maxCost:
                curN = r-l+1
                ans = max(curN, ans)
                r += 1
            else:
                if l == r:
                    l += 1
                    r += 1
                    currentCost = 0
                else:
                    currentCost -= (cost[l] + cost[r])
                    l += 1

        return ans

s = Solution()

print(s.equalSubstring("krrgw", "zjxss", 19))

print(s.equalSubstring("", "", 1))
print(s.equalSubstring("a", "b", 0))
print(s.equalSubstring("abcd", "bcdf", 0))
print(s.equalSubstring("abcd", "bcdf", 3))


print(s.equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
print(s.equalSubstring(s = "abcd", t = "acde", maxCost = 0))