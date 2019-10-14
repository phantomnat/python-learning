from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mem = {}
        for i in arr:
            mem[i] = mem.get(i, 0) + 1
        return len(mem.keys()) == len(set(mem.values()))

s = Solution()
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))