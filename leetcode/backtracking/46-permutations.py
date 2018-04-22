class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation = []

        self.mutate(nums, [], permutation)

        return permutation
    
    def mutate(self, nums, num_list, permutation):
        if len(nums) == 1:
            permutation.append(num_list + [nums[0]])
            return
        
        for i, n in enumerate(nums):
            self.mutate(nums[:i]+ nums[i+1:], num_list + [n], permutation)
            
if __name__ == '__main__':
    s = Solution()

    assert s.permute(
        [1,2,3]
    ) == [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]
