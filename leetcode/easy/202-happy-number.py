class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.is_happy(n, {n: 1})

    def is_happy(self, number, history = {}):
        if number == 1:
            return True

        # if n >= 10:
        n = number
        total = 0
        while n > 0:
            total += ((n % 10) ** 2)
            n //= 10
        
        # print('{} => {}'.format(number, total))
        if total in history:
            return False
        history[total] = 1
        return self.is_happy(total, history)
    
        
if __name__ == '__main__':
    s = Solution()

    print(s.isHappy(1))
    print(s.isHappy(2))
    print(s.isHappy(3))
    print(s.isHappy(4))
    print(s.isHappy(19))
    # print(s.getSum(-99, 33))