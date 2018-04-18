class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a >= 0 and b >= 0:
            return self.add(a, b)
        elif a <= 0 and b <= 0:
            return -self.add(-a, -b)
        else:
            a_pos = a if a >= 0 else -a
            b_pos = b if b >= 0 else -b
            neg = -1
            if a < 0 and b > a_pos:
                neg = 1
            elif b < 0 and a > b_pos:
                neg = 1

            return neg * self.sub(max(a_pos, b_pos), min(a_pos, b_pos))

    def add(self, a, b):
        # added = 0x1 & (a ^ b)
        carried = 0
        total = 0
        # a >>= 1
        # b >>= 1
        mark = 1
        while a > 0 or b > 0 or carried > 0:
            added = 0x1 & ((a ^ b) ^ carried)
            if added & 0x1:
                total |= (mark)
            carried = 0x1 & ((a & carried) or (b & carried) or (a & b))
            mark <<= 1
            a >>= 1
            b >>= 1

        return total
            
    def sub(self, a, b):
        carried = 0
        total = 0
        # a >>= 1
        # b >>= 1
        mark = 1
        while a > 0 or b > 0 or carried > 0:
            sub = 0x1 & ((a ^ b) ^ carried)
            if sub & 0x1:
                total |= (mark)
            c = 0x1 & ((~a & b) | (a & b & carried))
            carried = c
            mark <<= 1
            a >>= 1
            b >>= 1

        return total

if __name__ == '__main__':
    s = Solution()
    # s.getSum(-1, -1)
    # s.getSum(3, 2)
    # s.getSum(131, 222)
    # assert s.getSum(-1, -2) == -3
    # assert s.getSum(-5, 0) == -5
    # assert s.getSum(0, -6) == -6
    # print(s.getSum(-1, 2))
    print(s.getSum(-14, 16))
    # print(s.getSum(-99, 33))