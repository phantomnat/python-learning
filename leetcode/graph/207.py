# https://leetcode.com/problems/course-schedule/
# medium
# graph
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        paths = {i:[] for i in range(numCourses)}
        visited = [0 for i in range(numCourses)]
        for c,r in prerequisites:
            paths[r].append(c)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            elif visited[i] == 1:
                return True
            visited[i] = -1
            for n in paths[i]:
                if not dfs(n):
                    return False
            visited[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    #     visited = {}
    #     visiting = {}
    #     for i in range(numCourses):
    #         if i not in paths:
    #             continue
    #         if i in visited:
    #             continue

    #         if not self.dfs(paths, i, visited, visiting):
    #             return False
    #     return True

    # def dfs(self, paths, i, visited, visiting):
    #     visited[i] = True
    #     if i not in paths:
    #         return True

    #     visiting[i] = True
        
    #     for x in paths[i]:
    #         if x not in visited:
    #             if not self.dfs(paths, x, visited, visiting):
    #                 return False
    #         elif visiting.get(x, False):
    #             return False

    #     visiting[i] = False
    #     return True

s = Solution()
print(s.canFinish(2, [[1,0]]))
print(s.canFinish(4, [[0,1],[0,2],[2,1]]))
print(s.canFinish(4, [[0,1],[0,2],[2,1],[3,0],[1,3]]))
print(s.canFinish(4, [[0,1],[0,2],[2,1],[1,3]]))
print(s.canFinish(2, [[0,1],[1,0]]))
