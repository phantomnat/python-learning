from typing import List
from collections import deque

class Solution:
    def trapPointer(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l, r = 0, n-1
        lh, rh = height[l], height[r]
        
        water = 0
        
        while l < r:
            w = 0
            if lh <= rh:
                l+=1
                if lh <= height[l]:
                    lh = height[l]
                else:
                    w = min(lh,rh) - height[l]
            else:
                r-=1
                if rh <= height[r]:
                    rh = height[r]
                else:
                    w = min(lh,rh) - height[r]
            if w > 0:
                water += w
        
        return water

    def trapDP(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        lrheight = [[0,0] for i in range(n)]
        # for i in range(n):
            # lrheight[i] = [0,0]
        
        lh = rh = 0
        for l in range(n):
            r = n-l-1
            lh = max(height[l], lh)
            rh = max(height[r], rh)
            lrheight[l][0] = lh
            lrheight[r][1] = rh
        water = 0
        for i in range(n):
            water += min(lrheight[i]) - height[i]
        return water 

    def trapStack(self, height: List[int]) -> int:
        stack = deque()
        water = 0
        for h in height:
            if stack and h >= stack[0]:
                lh = stack.popleft()
                while stack:
                    ph = stack.pop()
                    water += min(lh, h) - ph

            stack.append(h)

        lh = stack.popleft()
        rh = 0
        while stack:
            ph = stack.pop()
            if ph >= rh:
                rh = ph
            else:
                water += min(lh,rh) - ph
        return water


s = Solution()
print([
    s.trapDP([0,1,0,2,1,0,1,3,2,1,2,1])
])