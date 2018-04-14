class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # I = 1
        # V = 5
        # X = 10
        # L = 50
        # C = 100
        # D = 500
        # M = 1000
        thousand = (num // 1000) * 1000
        hundred = ((num % 1000) // 100) * 100
        ten = ((num % 100) // 10) * 10
        digit = (num % 10)
        # print(thousand, hundred, ten, digit)
        ans = self.gen(thousand) + self.gen(hundred) + self.gen(ten) + self.gen(digit)
        # print(ans)
        return ans

    def gen(self, i):
        if i < 10:
            n1, n5, n10 = 'I', 'V', 'X'
        elif i < 100:
            i //= 10
            n1, n5, n10 = 'X', 'L', 'C'
        elif i < 1000:
            i //= 100
            n1, n5, n10 = 'C', 'D', 'M'
        else:
            i //= 1000
            n1, n5, n10 = 'M', None, None

        s = ''
        if n5 is None and n10 is None:
            s += n1 * i
        elif i < 5:
            s = n1 * i if i <= 3 else (n1 * (5 - i)) + n5
        elif i >= 5:
            if i >= 9 and n10 is not None:
                s = (n1 * (10 - i)) + n10
            else:
                s = n5 + (n1 * (i - 5))
        # print(s)
        return s

if __name__ == '__main__':
    s = Solution()
    assert s.intToRoman(1000) == 'M'
    assert s.intToRoman(40) == 'XL'
    assert s.intToRoman(7) == 'VII'
    assert s.intToRoman(8) == 'VIII'
    assert s.intToRoman(9) == 'IX'
    assert s.intToRoman(47) == 'XLVII'