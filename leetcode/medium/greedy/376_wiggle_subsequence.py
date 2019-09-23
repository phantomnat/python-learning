from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1: return 1 # need to be clear about this case

        l, r = 1, n-1
        count = 1
        lastNo, lastTurn = nums[0], 0
        
        while l < n:
            diff = nums[l] - lastNo
            if lastTurn == 0:
                if diff != 0:
                    count += 1
                    lastNo, lastTurn = nums[l], diff
            elif lastTurn > 0:
                # need lowest no
                if diff < 0:
                    count += 1
                    lastNo, lastTurn = nums[l], diff
                else:
                    lastNo = max(lastNo, nums[l])
            else:
                # < 0, highest no needed
                if diff > 0:
                    count += 1
                    lastNo, lastTurn = nums[l], diff
                else: 
                    lastNo = min(lastNo, nums[l])

            l += 1
     
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.wiggleMaxLength([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]))