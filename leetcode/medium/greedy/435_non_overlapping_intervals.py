class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        def sortFirst(v):
            return (v[0], v[1])
        
        n = len(intervals)
        if n <= 1:
            return 0
        
        intervals.sort(key=sortFirst)
        start, end = intervals[0]
        ans = 0
        for a in intervals[1:]:
            l, r = a
            if l == start:
                ans += 1
            elif l > start and l < end:
                ans += 1
                if r < end:
                    start, end = l, r
            else:
                start, end = l, r
        return ans
if __name__ == '__main__':
    s = Solution()
    # print(s.eraseOverlapIntervals([[2,3]]))
    print(s.eraseOverlapIntervals([[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9],[-92,-63],[-91,-76],[-90,-44],[-89,-18],[-88,10],[-87,-39],[-86,7],[-85,-76],[-84,-51],[-83,-48],[-82,-36],[-81,-63],[-80,-71],[-79,-4],[-78,-63],[-77,-14],[-76,-10],[-75,-36],[-74,31],[-73,11],[-72,-50],[-71,-30],[-70,33],[-69,-37],[-68,-50],[-67,6],[-66,-50],[-65,-26],[-64,21],[-63,-8],[-62,23],[-61,-34],[-60,13],[-59,19],[-58,41],[-57,-15],[-56,35],[-55,-4],[-54,-20],[-53,44],[-52,48],[-51,12],[-50,-43],[-49,10],[-48,-34],[-47,3],[-46,28],[-45,51],[-44,-14],[-43,59],[-42,-6],[-41,-32],[-40,-12],[-39,33],[-38,17],[-37,-7],[-36,-29],[-35,24],[-34,49],[-33,-19],[-32,2],[-31,8],[-30,74],[-29,58],[-28,13],[-27,-8],[-26,45],[-25,-5],[-24,45],[-23,19],[-22,9],[-21,54],[-20,1],[-19,81],[-18,17],[-17,-10],[-16,7],[-15,86],[-14,-3],[-13,-3],[-12,45],[-11,93],[-10,84],[-9,20],[-8,3],[-7,81],[-6,52],[-5,67],[-4,18],[-3,40],[-2,42],[-1,49],[0,7],[1,104],[2,79],[3,37],[4,47],[5,69],[6,89],[7,110],[8,108],[9,19],[10,2]]))
    # print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    # print(s.eraseOverlapIntervals([[2,3],[1,5],[1,2]]))