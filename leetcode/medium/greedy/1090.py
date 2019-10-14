# https://leetcode.com/problems/largest-values-from-labels/

from typing import List
import collections
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        n = len(values)
        vl = [(values[i], labels[i]) for i in range(n)]
        vl.sort(key=lambda x: (x[0], x[1]),reverse=True)
        mem = collections.defaultdict(int)
        ans = 0
        count = 0
        i = 0
        while count < num_wanted:
            v, l = vl[i]
            if mem[l] < use_limit:
                mem[l] += 1
                ans += v
                count += 1
            i += 1

        return ans

s = Solution()
print(s.largestValsFromLabels(
    [5,4,3,2,1], [1,1,2,2,3], 3, 1
))
print(s.largestValsFromLabels(
    [5,4,3,2,1], [1,3,3,3,2], 3, 2
))