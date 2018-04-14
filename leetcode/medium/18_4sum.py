class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, sorted_nums, target, N, result, results):
        n = len(sorted_nums)
            
        if N == 2:
            L = 0
            R = n - 1
            while L < R:
                A = sorted_nums[L]
                B = sorted_nums[R]
                s = A + B
                if s < target:
                    L += 1
                elif s > target:
                    R -= 1
                else:
                    results.append(result + [A, B])
                    while L + 1 < n and A == sorted_nums[L]:
                        L += 1
                    while R > 0 and B == sorted_nums[R]:
                        R -= 1
        else:
            for i in range(n-N+1):
                if target < sorted_nums[i] * N or target > sorted_nums[-1] * N:
                    break
                if (i == 0) or (i > 0 and sorted_nums[i] != sorted_nums[i-1]):
                    self.findNsum(sorted_nums[i+1:], target-sorted_nums[i], N-1, result+[sorted_nums[i]], results)
 
if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(s.fourSum([-1,0,1,2,-1,-4]))
    # print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
    # print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    
    # print(s.threeSum([13,4,-6,-7,-15,-1,0,-1,0,-12,-12,9,3,-14,-2,-5,-6,7,8,2,-4,6,-5,-10,-4,-9,-14,-14,12,-13,-7,3,7,2,11,7,9,-4,13,-6,-1,-14,-12,9,9,-6,-11,10,-14,13,-2,-11,-4,8,-6,0,7,-12,1,4,12,9,14,-4,-3,11,10,-9,-8,8,0,-1,1,3,-15,-12,4,12,13,6,10,-4,10,13,12,12,-2,4,7,7,-15,-4,1,-15,8,5,3,3,11,2,-11,-12,-14,5,-1,9,0,-12,6,-1,1,1,2,-3]))
    # print(s.threeSum([-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]))