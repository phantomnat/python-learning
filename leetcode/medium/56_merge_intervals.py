class Solution:
    def merge(self, intervals):
        def sortKey(v):
            return (v[0], v[1])
        
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(key=sortKey)
        ans = []
        start, end = intervals[0]
        for (l,r) in intervals[1:]:
            # is overlapping
            is_overlapping = l <= end
            if is_overlapping:
                start, end = min(start, l), max(end, r)
            else:
                ans.append([start, end])
                start, end = l, r
        ans.append([start, end])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))