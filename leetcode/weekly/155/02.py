# import math
import heapq

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # l, r = 1, 2 * 10**9
        # x, y, z = a * b // math.gcd(a, b), b * c // math.gcd(b, c), a * c // math.gcd(a, c)
        # w = x * y // math.gcd(x, y)
        # ans = 0
        # while l <= r:
        #     mid = (l + r) // 2
        #     cnt = mid // a + mid // b + mid // c - mid // x - mid // y - mid // z + mid // w
        #     if cnt >= n:
        #         r = mid - 1
        #         if cnt == n:
        #             ans = mid
        #     else:
        #         l = mid + 1
        # return ans

        nums = [[a,a], [b,b], [c,c]]
        nums.sort(key=lambda x: (x[0], x[1]))
        i = 1
        while True:
            if i == n: return nums[0][0]
            diff = nums[1][0] - nums[0][0]
            step = diff // nums[0][1]
            if step == 0:
                if nums[0][0] == nums[1][0]:
                    nums[1][0] += nums[1][1]
                if nums[0][0] == nums[2][0]:
                    nums[2][0] += nums[2][1]

                nums[0][0] += nums[0][1]
                i += 1
            else:
                if step > n-i:
                    return nums[0][0] + (nums[0][1] * (n-i))
                nums[0][0] = nums[0][0] + (nums[0][1] * step)
                i += step

            nums.sort(key=lambda x: (x[0], x[1]))

        return 0

if __name__ == '__main__':
    s = Solution()
    # print(s.nthUglyNumber(3,2,3,5))
    print(s.nthUglyNumber(5,2,3,3))
    print(s.nthUglyNumber(4,2,3,4))
    print(s.nthUglyNumber(1000000000,2,217983653,336916467))