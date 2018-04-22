class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zero = 0
        factor = 5
        z = n // factor
        while z > 0:
            zero += z
            factor *= 5
            z = n // factor
    
        return zero
    
if __name__ == '__main__':
    s = Solution()
    # assert s.trailingZeroes(1000) == 6
    assert s.trailingZeroes(30) == 7
    # print(s.isHappy(1))
    # print(s.isHappy(2))
    # print(s.isHappy(3))
    # print(s.isHappy(4))
    # print(s.isHappy(19))