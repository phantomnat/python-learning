class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        val = 0
        mul = 1
        is_num = False
        for c in str:
            if not is_num and c == ' ':
                pass
            elif not is_num and c == '+':
                is_num = True
            elif not is_num and c == '-':
                is_num = True
                mul = -1
            elif c >= '0' and c <= '9':
                val = (val * 10) + int(c)
                is_num = True
            else:
                break

        val *= mul
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if val > MAX_INT: return MAX_INT
        if val < MIN_INT: return MIN_INT
        return val

s = Solution()
print(s.myAtoi("  -0012a42"))
print(s.myAtoi(" +-1"))
