class Solution:
    def numberOfArithmeticSlices(self, A: list) -> int:
        n = len(A)
        ans = 0

        mem={}
    
        for i in range(1, n):
            # _ans = 0
            for j in range(i):
                dist = A[i]-A[j]
                key = f'{i},{dist}'

                ss = mem.get(f'{j},{dist}', 0)
                ans += ss
                # add weak subsequence
                mem[key] = mem.get(key, 0) + 1 + ss

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 1, 2, 3, 4, 5]), '= 11')
    print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]), '= 7')
    print(s.numberOfArithmeticSlices([7, 7, 7, 7]))
    print(s.numberOfArithmeticSlices([3, -1, -5, -9]))
    print(s.numberOfArithmeticSlices([1, 1, 2, 5, 7]))
    print(s.numberOfArithmeticSlices([0,1,2,2,2]), ' =  4')
    print(s.numberOfArithmeticSlices([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), ' =  ?')
    print(s.numberOfArithmeticSlices([1,2,3,4,5,6,7]), ' =  20')

# 1, 2, 3, 4, 5, 6, 7
# 0, 1, 2, 3, 4, 5
# 0, 0, 1, 2, 4, 4, 5
#                1, 2
#                   1

# 1
# 1
# 2
# 3
# 4