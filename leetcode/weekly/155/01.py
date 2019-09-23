from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        minDiff = 1000000000
        mem = {x:True for x in arr}
        ans = []
        # find min dist
        for i in range(1, n):
            diff = abs(arr[i] - arr[i-1])
            minDiff = min(minDiff, diff)
        for i in range(0, n):
            if arr[i]+minDiff in mem:
                ans.append([arr[i], arr[i]+minDiff])
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.minimumAbsDifference([1]))
    # print(s.minimumAbsDifference([]))
    print(s.minimumAbsDifference([4,2,1,3]))
    print(s.minimumAbsDifference([1,3,6,10,15]), ' = [[1,3]]')
    print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))