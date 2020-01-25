# https://leetcode.com/problems/divide-two-integers/
# 

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        
        
        isPositive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor

        ans = 0
        divisors = {0: 0, 1: divisor}
        divIdx = 1

        while divisors[divIdx] < dividend:
            i = divIdx
            divIdx += divIdx
            divisors[divIdx] = divisors[i] + divisors[i]
    
        divisorsKeys = sorted(list(divisors.keys()))
        divisorsIdx = len(divisorsKeys)-1

        while divisorsIdx > 0 and dividend > 0:
            while divisors[divisorsKeys[divisorsIdx]] > dividend:
                divisorsIdx -= 1
            dividend -= divisors[divisorsKeys[divisorsIdx]]
            ans += divisorsKeys[divisorsIdx]
        
        return ans if isPositive else -ans

s = Solution()
# print(s.divide(10,3))
print(s.divide(10,-2))
print(s.divide(100000000000,-2))