class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev_val = 0
        val = x

        while val > 0:
            rev_val = (rev_val * 10) + (val % 10)
            val //= 10
        
        return x == rev_val

if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(1)
    s.isPalindrome(1221)
    assert s.isPalindrome(10) == False