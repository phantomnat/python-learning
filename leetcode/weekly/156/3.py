from typing import List
from collections import defaultdict

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        newS = list(s)
        isFound = True
        while isFound:
            isFound = False
            S = list(newS)
            n = len(S)
            if n == 0: return ''
            newS = []
            lastChar, lastCount = '', 0
            i = 0
            while i < n:
                if not lastChar:
                    lastChar, lastCount = S[i], 1
                elif lastChar != S[i]:
                    newS.extend([lastChar]*lastCount)
                    lastChar, lastCount = S[i], 1
                else:
                    lastCount += 1
                    if lastCount == k:
                        isFound = True
                        lastChar, lastCount = '', 0
                i += 1
            if lastChar and lastCount:
                newS.extend([lastChar]*lastCount)
        return ''.join(newS)
            
            

s = Solution()
print(s.removeDuplicates(s = "abcd", k = 2))
print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))