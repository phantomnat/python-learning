# https://leetcode.com/problems/flower-planting-with-no-adjacent/
# easy
# graph

from typing import List

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        gardens = {i:[] for i in range(1,N+1)}
        visited = {}
        for i,j in paths:
            gardens[i].append(j)
            gardens[j].append(i)
        ans = [0]*N
        for i in range(1,N+1):
            ans[i-1] = ({1,2,3,4} - {ans[x-1] for x in gardens[i]}).pop()
        return ans

        # gardens = {i:set() for i in range(1,N+1)}
        # visited = {}
        # for i,j in paths:
        #     gardens[i].add(j)
        #     gardens[j].add(i)
    
        # for i in range(1,N+1):
        #     if i in visited:
        #         continue
        #     f = {1,2,3,4} - {visited.get(x, '-1') for x in gardens[i]}
        #     visited[i] = (list(f)).pop(0)

        # return [visited[x+1] for x in range(N)]

s = Solution()
# print(s.gardenNoAdj(3,[[1,2],[2,3],[3,1]]))
print(s.gardenNoAdj(4,[[1,2],[3,4]]))
print(s.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
print(s.gardenNoAdj(5, [[1,2], [2,3], [3,4], [4,5], [2,5], [5,1], [3,1]]))
