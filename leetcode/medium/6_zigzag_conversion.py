class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        lines = [''] * numRows

        row = 0
        direction = 1
        for i in range(n):
            lines[row] += s[i]
            
            if row + direction >= numRows:
                direction = -1
            elif row + direction < 0:
                direction = 1

            row += direction
            
        # print(lines)
        return ''.join(lines)

if __name__ == '__main__':
    s = Solution()
    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("A", 1) == "A"
    assert s.convert("ABCDEFG", 2) == "ACEGBDF"
    