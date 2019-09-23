# https://leetcode.com/problems/remove-k-digits/
# medium
# 

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == 0:
            return num
        elif k == n:
            return '0'

        out = []
        for d in num:
            while k and out and out[-1] > d:
                k -= 1
                out.pop()
            out.append(d)
        
        return ''.join(out[:-k or None]) or '0'

        # maxAns = int(num[0])
        # ans = [int(num[0])]
        # count = 1
        # removed = 0
        # for i in range(1, n):
        #     rem = 0
        #     nAns = len(ans)
        #     if int(num[i]) == 0 and nAns == 1:
        #         ans[-1] *= 10
        #         maxAns = max(ans)
        #     else:
        #         while int(num[i]) < maxAns and rem < nAns:
        #             rem += 1
        #             if removed + rem == k:
        #                 return answer(''.join(str(x) for x in ans[:nAns-rem]) + num[count:])
        #             maxAns = ans[nAns-rem-1]
        #         ans = ans[:nAns-rem]                
        #         removed += rem
        #         ans.append(int(num[i]))
        #         maxAns = max(ans)
                
        #     count += 1
        # if k > removed:
        #     ans = ans[:len(ans)-(k-removed)]
        # return answer(''.join(str(x) for x in ans) + num[count:])



if __name__ == '__main__':
    s = Solution()
    # print(s.removeKdigits("10200", 1), ' 200')
    print(s.removeKdigits("4321", 2), ' 21')
    print(s.removeKdigits("1090200", 1), ' 90200')
    print(s.removeKdigits("1090200", 2), ' 200')
    print(s.removeKdigits("1090200", 3), ' 200')
    print(s.removeKdigits("1234511", 4), ' 111')
    print(s.removeKdigits("1234599", 4), ' 123')
    print(s.removeKdigits("1912345", 1), ' 112345')
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("1432519", 3))
    print(s.removeKdigits("1432519", 3))
    print(s.removeKdigits("1234567", 3), ' 1234')
    print(s.removeKdigits("1492519", 1))
    print(s.removeKdigits("142519", 1))
    print(s.removeKdigits("942519", 1))
    print(s.removeKdigits("192519", 1))
    print(s.removeKdigits("132519", 1))
    print(s.removeKdigits("1132519", 3), '1119')
    print(s.removeKdigits("1132119", 3), '1111')
    # print(s.removeKdigits("1132519", 1))
    # print(s.removeKdigits("1111199", 1))