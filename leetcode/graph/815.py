# https://leetcode.com/problems/bus-routes/
# hard
# 

from typing import List
from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        routeToRoutes = defaultdict(set)
        busStopToRoutes = defaultdict(set)
        for i, busStop in enumerate(routes):
            for bs in busStop:
                busStopToRoutes[bs].add(i)

        startRoute = set(busStopToRoutes[S])
        endRoute = set(busStopToRoutes[T])

        for route, busStop in enumerate(routes):
            for bs in busStop:
                routes = busStopToRoutes[bs]
                routeToRoutes[route] |= (routes - {route})
        
        search = endRoute
        next = set()
        visited = {}
        count = 1
        while search:
            r = search.pop()
            visited[r] = 1
            if r in startRoute:
                return count
            for i in routeToRoutes[r]:
                if i in visited:
                    continue
                next.add(i)
            if not search:
                count += 1
                search, next = next, set()
        return -1
s = Solution()
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]],1,6))
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7], [5,4]],5,3))
print(s.numBusesToDestination([[1], [3], [5,4]],1,1))
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7], [5,4],[4,8,2],[4,9,10]],5,3))
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7, 9], [5,4],[4,8,2],[4,9,10]],5,3))