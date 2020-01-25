from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r,p = 0,n-1,0
        while l <= r:
            m = l+(r-l)//2
            if nums[m-1] > nums[m]:
                p = m
                break
            elif m+1 < n and nums[m] > nums[m+1]:
                p=m+1
                break
            elif nums[l] < nums[r]:
                p=l
                break
            else:
                if nums[l] < nums[m]:
                    l = m+1
                else:
                    r = m-1
        print(p)
        l,r = 0,n-1
        while l <= r:
            m = l+(r-l)//2
            mi = m+p if m+p<n else m+p-n
            if nums[mi] == target:
                return mi
            elif nums[mi] < target:
                l = m+1
            else:
                r = m-1
        return -1
            
s = Solution()
# print(s.search([3,1], 1))
# print(s.search([3,1], 2))
print(s.search([3], 3))
print(s.search([3], 2))