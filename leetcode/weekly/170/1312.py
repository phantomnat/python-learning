import collections
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        mem = [[0] * n for _ in range(n)]

        for i in range(n):
            mem[i][i] = 1
            for j in range(i-1,-1,-1):
                if s[i] == s[j]:
                    mem[i][j] = mem[i-1][j+1] + 2
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j+1])
        
        return n - mem[n-1][0]

s = Solution()
print(s.minInsertions('zzazz'))
print(s.minInsertions('mbadm'))
print(s.minInsertions('leetcode'))