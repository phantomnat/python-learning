class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_area = 0
        l, r = 0, n - 1
        while l < r:
            max_area = max(min(height[l],height[r]) * (r - l), max_area)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         # print(i, j)
        #         area = min(height[i],height[j]) * (j - i)
        #         if area > max_area:
        #             max_area = area

        # print(max_area)
        return max_area

if __name__ == '__main__':
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    