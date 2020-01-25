from typing import List

class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        l,r = 0,len(nums)-k

        while l<r:
            m=(l+r)//2
            if x-nums[m] > nums[m+k]-x:
                l = m+1
            else:
                r = m
        return nums[l:l+k]

    # def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
    #     if not nums: return []
    #     # nums = [n-x for n in nums]
    #     n = len(nums)
        
    #     l,r = 0, n-1
    #     while l < r:
    #         m=(l+r)//2
    #         if nums[m] < x:
    #             l = m+1
    #         else:
    #             r = m
        
    #     if nums[l] == x:
    #         lb = l
    #         # find right bound
    #         l,r = lb, n-1
    #         while l<r:
    #             m=(l+r+1)//2
    #             if nums[m] > x:
    #                 r = m-1
    #             else:
    #                 l = m
    #         rb = r
    #         if rb-lb+1 >= k:
    #             return [x]*k
    #     else:
    #         lb, dif = l, abs(nums[l]-x)
    #         if l-1 >= 0 and abs(nums[l-1]-x) < dif:
    #             lb, dif = l-1, abs(num[l-1]-x)
    #         if l+1 < n and abs(nums[l+1]-x) < dif:
    #             lb, dif = l+1, abs(num[l+1]-x)
    #         rb = lb
        
    #     while rb-lb+1 < k:
    #         if lb == 0:
    #             rb += k-rb+lb-1
    #             break
    #         elif rb == n-1: 
    #             lb -= k-rb+lb-1
    #             break

    #         if abs(nums[lb-1]-x) <= abs(nums[rb+1]-x):
    #             lb -= 1
    #         else:
    #             rb += 1

    #     return nums[lb:lb+(rb-lb+1)]

s = Solution()
ans = [
    s.findClosestElements([0,1,2,2,2,3,6,8,8,9],5,9),
    s.findClosestElements([1], 1, 0),
    s.findClosestElements([1,1,1,10,10,10], 3, 9),
    s.findClosestElements([1,1,2,2,2,3,3], 5, 2),
s.findClosestElements([0,1,2,2,2,3,3], 5, 2),
]
print(ans)