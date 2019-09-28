# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# hard
# graph,dfs,topological-search

from typing import List
from collections import defaultdict
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graphGroup = defaultdict(set)
        graphItem = {}
        for i,g in enumerate(group):
            if g == -1:
                g = group[i] = m
                m += 1
            graphItem[g] = graphItem.get(g, {})
            graphItem[g][i] = []

        for after, befores in enumerate(beforeItems):
            for before in befores:
                ga, gb = group[after], group[before]
                if ga == gb:
                    graphItem[ga][after].append(before)
                else:
                    graphGroup[ga].add(gb)
        
        groupOrder = []
        groupVisited = [0] * m

        # print(graphGroup)

        def hasCycle(i, visited, graph, ans):
            if visited[i] == -1:   # visiting
                return True
            if visited[i] == 1:
                return False
            visited[i] = -1
            for x in graph[i]:
                if hasCycle(x, visited, graph, ans):
                    return True
            visited[i] = 1
            ans.append(i)
            return False

        for i in range(m):
            if hasCycle(i, groupVisited, graphGroup, groupOrder):
                return []

        ans=[]
        
        for g in groupOrder:
            if g not in graphItem:
                continue
            visited = [0]*n
            for i in graphItem[g].keys():
                if hasCycle(i, visited, graphItem[g], ans):
                    return []
        
        return ans

s = Solution()

# print(s.sortItems(8,2,[-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]))
# print(s.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))
print(s.sortItems(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]]))

#   2 -> 5,0,3

# 0   2   2,1,3
# 1   0   2,4
# 2   5   
# 3   3
# 4   0
