from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        n=len(nums)
        if n==1: return nums[0]
        l,r=0,n-1
        while l<=r:
            if nums[l] <= nums[r]:
                break
                
            m = l+(r-l)//2
            if nums[l] <= nums[m]:
                l=m+1
            else:
                r=m
          
        return nums[l]
                
s = Solution()
s.findMin([2,1])