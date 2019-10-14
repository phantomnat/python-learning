from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        maxDist = 0
        lastSeatedIdx = -1
        dist = 0
        for i, s in enumerate(seats):
            if s == 1:
                # seated
                if lastSeatedIdx == -1:
                    maxDist = max(maxDist, i)
                else:
                    dist = i - lastSeatedIdx
                    maxDist = max(maxDist, dist//2)
                
                lastSeatedIdx = i
                
        maxDist = max(maxDist, n-lastSeatedIdx-1)
        return maxDist

s = Solution()
print(s.maxDistToClosest([1,0,0,1]), " - 1")
print(s.maxDistToClosest([0,0,0,1]), " - 3")
print(s.maxDistToClosest([1,0,0,0]))
print(s.maxDistToClosest([1,0,0,0,1,0,1]))