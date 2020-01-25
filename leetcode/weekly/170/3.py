import collections
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        watchedVids = collections.defaultdict(int)
        visited = collections.defaultdict(bool)
        lv = 0
        search = [id]
        nextSearch = []
        while search:
            _id = search.pop(0)
            if visited[_id]:
                continue
    
            visited[_id] = True
            
            # add friend to next search
            for f in friends[_id]:
                if not visited[f]:
                    nextSearch.append(f)
            
            if lv == level:
                for v in watchedVideos[_id]:
                    watchedVids[v] += 1
            
            if not search:
                lv += 1
                if lv > level:
                    break
                search, nextSearch = nextSearch, []
                
        sortedWatchedVids = sorted(watchedVids.items(), key=lambda x: (x[1], x[0]))
        return [x[0] for x in sortedWatchedVids]

s = Solution()
print(s.watchedVideosByFriends([["A","B"],["C"],["B"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 1))