from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0

        n = len(arr)
        sortedArr = sorted(arr)
        prefixArr = sortedArr[:]
        for i in range(1, n):
            prefixArr[i] += prefixArr[i-1]
        
        lv, rv = sortedArr[0], sortedArr[-1]
        total = sum(sortedArr)
        
        def searchArr(arr, t):
            l,r = 0,len(arr)
            while l<r:
                m = (l+r+1)//2
                if arr[m] > t:
                    r=m-1
                else:
                    l=m
            return l
        
        if target < lv*n:
            l, r = 0, (target//n)+1
            while l+1<r:
                m = (l+r)//2
                if m*n == target:
                    return m
                elif m*n > target:
                    r=m-1
                else:
                    l=m
            return l if abs(target-l*n) <= abs(target-r*n) else r
        elif target >= total:
            return rv
        
        l,r = lv, rv
        # binary search
        while l+1 < r:
            mv = (l+r)//2
            mi = searchArr(sortedArr, mv)

            t = prefixArr[mi] + mv*(n-mi-1)
            if t == target:
                return mv
            elif t > target:
                r = mv
            else:
                l = mv

        li = searchArr(sortedArr, l)
        tl = prefixArr[li] + l*(n-li-1)
        dl = abs(target - tl)
        ri = searchArr(sortedArr, r)
        tr = prefixArr[ri] + r*(n-ri-1)
        dr = abs(target - tr)
        return l if dl <= dr else r
s = Solution()
print([
    # s.findBestValue([4,9,3], 10),
    # s.findBestValue([2,3,5], 10),
    # s.findBestValue([60864,25176,27249,21296,20204], 56803),
    # s.findBestValue([1547,83230,57084,93444,70879], 71237),
    # s.findBestValue([1547,83230,57084,93444,70879], 467216),
    # s.findBestValue([1547,83230,57084,93444,70879], 467219),
    s.findBestValue([1547,83230,57084,93444,70879], 467219),
    # s.findBestValue([60864,25176,27249,21296,20204], 56803)
])