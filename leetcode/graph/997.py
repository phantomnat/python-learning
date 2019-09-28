# https://leetcode.com/problems/find-the-town-judge/
# easy
# graph

from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC%2B%2BPython-Directed-Graph
        count = [0] * (N + 1)
        for i,j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N+1):
            if count[i] == N-1:
                return i
        return -1

        # otherTrust = {}
        # trustOther = {}
        # if N == 1 and not trust:
        #     return 1
        # for src,dest in trust:
        #     otherTrust[dest] = otherTrust.get(dest, []) 
        #     otherTrust[dest].append(src)
        #     trustOther[src] = trustOther.get(src, []) 
        #     trustOther[src].append(dest)

        # for p,v in otherTrust.items():
        #     if len(v) == N-1 and p not in trustOther:
        #         return p
        # return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(2, [[1,2]]), ' = 2')
    print(s.findJudge(3, [[1,3],[2,3]]), ' = 3')
    print(s.findJudge(3, [[1,3],[2,3],[3,1]]), ' = -1')
    print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), ' = 3')