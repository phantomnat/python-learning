from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        ans = -1
        while l<r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        if nums[r] != target:
            return [-1,-1]
        ans = r
        l,r=r,len(nums)-1
        while l<r:
            m = (l+r+1)//2
            if nums[m] > target:
                r = m-1
            else:
                l = m
        return [ans, l]

s = Solution()
ans = [
    s.searchRange([1],0),
    s.searchRange([5,7,7,8,8,8,9,10],8),
    s.searchRange([7,7,7,8,10],7),
    s.searchRange([7,7,7,8,10,10,10,10],10),
    s.searchRange([7,7,7,8,10],10),
    s.searchRange([7,7,7,7,8,10],10),
]
for a in ans:
    print(a)