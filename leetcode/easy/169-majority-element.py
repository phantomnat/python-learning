class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums[0]
        min_element = len(nums) // 2
        num_dict = {}
        for n in nums:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                if num_dict[n] + 1 > min_element:
                    return n
                num_dict[n] += 1

if __name__ == '__main__':
    s = Solution()
    assert s.majorityElement([10, 10, 10, 3, 4, 4]) == 7