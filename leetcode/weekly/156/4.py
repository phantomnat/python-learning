
from typing import List
from collections import defaultdict

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        snackRotation = '-'
        n = len(grid)
        pos = [0,0]
        def canGo(grid, n, pos, rot, mem, lastMove, target=(0,0)):
            up = left = rotate = 100000000
            key=f'{pos[1]}_{pos[0]}_{rot}'
            if pos == target and rot == '-':
                return 0
            if key in mem:
                return mem[key]
            if rot == '-':
                if pos[0]-1 >= 0 and \
                    grid[pos[0]-1][pos[1]] == 0 and grid[pos[0]-1][pos[1]+1] == 0:
                    up = 1+canGo(grid, n, (pos[0]-1,pos[1]), rot, mem, 'up')
                if pos[1]-1 >= 0 and \
                    grid[pos[0]][pos[1]-1] == 0:
                    left = 1+canGo(grid, n, (pos[0],pos[1]-1), rot, mem, 'left')
                if pos[0]+1 < n and lastMove != 'rotate' and \
                    grid[pos[0]][pos[1]] == 0 and grid[pos[0]][pos[1]+1] == 0 and \
                    grid[pos[0]+1][pos[1]] == 0 and grid[pos[0]+1][pos[1]+1] == 0:
                    rotate = 1+canGo(grid, n, (pos[0],pos[1]), '|', mem, 'rotate')
            else:
                if pos[0]-1 >= 0 and \
                    grid[pos[0]-1][pos[1]] == 0:
                    up = 1+canGo(grid, n, (pos[0]-1,pos[1]), rot, mem, 'up')
                if pos[1]-1 >= 0 and pos[0]+1 < n and \
                    not grid[pos[0]][pos[1]-1] and not grid[pos[0]+1][pos[1]-1]:
                    left = 1+canGo(grid, n, (pos[0],pos[1]-1), rot, mem, 'left')
                if pos[0]+1 < n and lastMove != 'rotate' and \
                    grid[pos[0]][pos[1]] == 0 and grid[pos[0]][pos[1]+1] == 0 and \
                    grid[pos[0]+1][pos[1]] == 0 and grid[pos[0]+1][pos[1]+1] == 0:
                    rotate = 1+canGo(grid, n, (pos[0],pos[1]), '-', mem, 'rotate')
            mem[key] = min(up, left, rotate)
            return mem[key]
            # up = ca
        mem = {}
        ans = canGo(grid, n, (n-1, n-2), '-', mem, '')
        return -1 if ans == 100000000 else ans

s = Solution()

# print(s.minimumMoves(grid = [
#     [0,0,0,0,0,1],
#     [1,1,0,0,1,0],
#     [0,0,0,0,1,1],
#     [0,0,1,0,1,0],
#     [0,1,1,0,0,0],
#     [0,1,1,0,0,0]]
# ))
                
print(s.minimumMoves(grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,1,0,0,1],
    [0,1,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0]]
))
print(s.minimumMoves(grid = [
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,1,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,1,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0]]
))
