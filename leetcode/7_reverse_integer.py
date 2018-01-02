class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        y = int(a[::-1]) if x >= 0 else int(a[1:][::-1]) * -1
        if y < -2147483648 or y > 2147483647: return 0
        return y
    
s = Solution()
print(s.reverse(-210))
