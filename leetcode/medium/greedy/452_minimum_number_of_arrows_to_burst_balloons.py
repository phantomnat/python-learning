class Solution:
    def findMinArrowShots(self, points) -> int:
        def sortKey(a):
            return (a[0], a[1])
        n = len(points)
        if n == 0:
            return 0
        points.sort(key=sortKey)
        ans = 1
        start, end = points[0]
        for (l, r) in points[1:]:
            if l <= end:
                start, end = max(l, start), min(end, r)
            else:
                start, end = l, r
                ans += 1

        return ans 

if __name__ == '__main__':
    s = Solution()
    # print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
    print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
