from typing import List
import collections

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        mem = {} # (l,u,r,d)
        def dp(grid, y, x, n, m, move, mem, visited={}):

            moves = {1,2,3,4} # up, down, left, right

            if (y,x) in visited:
                return 0
            visited[(y,x)]=True
            # if (y,x,move) in mem:
            #     return max(mem[(y,x,move)])
            if grid[y][x] == 0:
                return 0

            gold = grid[y][x]
            up = down = left = right = gold
            if y-1 >= 0:
                up += dp(grid, y-1, x, n, m, 1, mem,dict(visited))
            if y+1 < n:
                down += dp(grid, y+1, x, n, m, 2,mem, dict(visited))
            if x-1 >= 0:
                left += dp(grid, y, x-1, n, m, 3, mem, dict(visited))
            if x+1 < m:
                right += dp(grid, y, x+1, n, m, 4, mem, dict(visited))

            mem[(y,x,move)] = (up,down,left,right)
            return max(up,down,left,right)

        v = 0
        n = len(grid)
        m = len(grid[0])
        for y in range(n):
            for x in range(m):
                mem = {}
                if grid[y][x]:
                    v = max(v, dp(grid, y, x, n, m, set(), mem, {}))
                    print(sorted(list(mem.items()), key=lambda x: (x[0])))
        return v    

s = Solution()
# print(s.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
# print(s.getMaximumGold([
#     [0,6,0],
#     [5,8,7],
#     [0,9,0]]))
print(s.getMaximumGold([
    [1,0,7,0,0,0],
    [2,0,6,0,1,0],
    [3,5,6,7,4,2],
    [4,3,1,0,2,0],
    [3,0,5,0,20,0]
    ]))
# print(s.getMaximumGold([
#     [5 ,3 ,36,26,27],
#     [11,31,23,30,4],
#     [5 ,7 ,21,38,10],
#     [39,30,10,17,13],
#     [16,0 ,0 ,26,1],
#     [25,0 ,10,0 ,0]
#     ]))