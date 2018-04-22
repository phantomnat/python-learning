class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = []
        n = len(nums)
        
        for i in range(1, n+1):
            self.subset(nums[:], i, [], subsets)

        subsets.append([])

        return subsets
            
    def subset(self, nums, max_len, num_list, subsets):
        if len(num_list) + 1 == max_len and len(nums) > 0:
            for n in nums:
                subsets.append(num_list + [n])
            return
        elif len(nums) + len(num_list) < max_len:
            return
        
        while len(nums) > 0:
            n = nums.pop(0)
            self.subset(nums[:], max_len, num_list + [n], subsets)

if __name__ == '__main__':
    s = Solution()

    assert s.subsets(
        [1,2,3]
    ) == [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]
