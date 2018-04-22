class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = set()
       
        min_element = len(nums) // 3
        num_dict = {}
        for n in nums:
            if n not in num_dict:
                if 1 > min_element:
                    ans.add(n)
                num_dict[n] = 1
            else:
                if num_dict[n] + 1 > min_element:
                    ans.add(n)
                num_dict[n] += 1

        return list(ans)

if __name__ == '__main__':
    s = Solution()
    assert s.majorityElement([]) == []
    # assert s.majorityElement([1]) == [1]
    # assert s.majorityElement([1,2]) == [1,2]
    assert s.majorityElement([3,2,3]) == [3]
    assert s.majorityElement([10, 10, 10, 3, 4, 4]) == 7
    assert s.majorityElement([10, 10, 10, 3, 4, 4]) == 7