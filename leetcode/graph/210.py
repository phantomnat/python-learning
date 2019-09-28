# https://leetcode.com/problems/course-schedule-ii/
# medium
# graph
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Node Indegree
        indegrees = {}
        paths = {}
        # paths = {[] for _ in range(numCourses)}
        for c,r in prerequisites:
            indegrees[c] = indegrees.get(c, 0)+1
            paths[r] = paths.get(r, [])
            paths[r].append(c)
        ans = []
        search = [x for x in range(numCourses) if x not in indegrees]
        while search:
            v = search.pop(0)
            ans.append(v)

            if v in paths:
                for n in paths[v]:
                    indegrees[n] -= 1

                    if indegrees[n] == 0:
                        search.append(n)
        return ans if len(ans) == numCourses else []

        # dfs
        paths = {i:[] for i in range(numCourses)}
        visited = [0 for i in range(numCourses)]
        for c,r in prerequisites:
            paths[r].append(c)
        ans = []
        def dfs(i, ans):
            if visited[i] == -1:
                return False
            elif visited[i] == 1:
                return True
            visited[i] = -1
            for n in paths[i]:
                if not dfs(n, ans):
                    return False
            visited[i] = 1
            ans.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i, ans):
                return []
        return ans[::-1]

s = Solution()
# print(s.findOrder(2, [[1,0]]))
# print(s.findOrder(4, [[0,1],[0,2],[2,1]]))
print(s.findOrder(5, [[0,1],[0,2],[2,1],[3,0],[1,3]]))
# print(s.findOrder(4, [[0,1],[0,2],[2,1],[1,3]]))
print(s.findOrder(2, [[0,1],[1,0]]))
# print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# print(s.findOrder(10, [[1,0],[2,0],[3,1],[3,2]]))
