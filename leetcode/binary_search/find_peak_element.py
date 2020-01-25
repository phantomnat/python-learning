from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return 0
        n=len(nums)
        if n == 1: return 0
        l,r=0,n-1
        while l<r:
            m = l+(r-l)//2
            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m
  
        return r

s = Solution()
s.findPeakElement([1,2])
s.findPeakElement([2,1])
s.findPeakElement([1,2,3])
s.findPeakElement([3,2,1])
s.findPeakElement([1,2,3,1])
s.findPeakElement([1,2,1,3,5,6,4])