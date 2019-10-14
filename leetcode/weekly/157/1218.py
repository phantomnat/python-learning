from typing import List
import collections

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mem = collections.defaultdict(int)

        # def dp(arr, n, i, diff, mem):
        #     num = arr[i]
        #     key = (i,arr[i]+diff)
        #     if key in mem:
        #         return mem[key]
        #     v = 0
        #     for j in range(i+1, n):
        #         if arr[j] - num  == diff:
        #             v = max(v, 1 + dp(arr, n, j, diff, mem))
        #     mem[key] = v           
        #     return v
        
        n = len(arr)
        v=0
        for i in range(n-1,-1,-1):
            mem[arr[i]] = max(mem[arr[i]], 1+mem[arr[i]+difference])
            v = max(mem[arr[i]], v)
        # print(mem)
        return v
        # for i in range(n):
            # v = max(v, 1+dp(arr, n, i, difference, mem))
        # print(sorted(list(mem.items()),key=lambda x: (x[0][0],x[0][1])))
        # return v

s = Solution()
print(s.longestSubsequence([1,2,3,4], 1))
print(s.longestSubsequence([1,3,5,7], 1))
print(s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))
print(s.longestSubsequence([7,-2,8,10,6,18,9,-8,-5,18,13,-6,-17,-1,-6,-9,9,9], 1))
print(s.longestSubsequence([7,8,10,9,11,10,11], 1))
