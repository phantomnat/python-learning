# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# graph, dfs

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        