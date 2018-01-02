class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        
        ele1_idx = (n + m) // 2
        ele2_idx = 0
        if (n+m) % 2 == 0: ele2_idx = ele1_idx + 1
        else: ele1_idx += 1
        # print('elem1', ele1_idx, '  elem2',ele2_idx)
        
        i1 = i2 = cur_idx = val = 0
        ele1_match = False
        ele2_match = False if ele2_idx > 0 else True
        while not ele1_match or not ele2_match:
            i1_lower = False
            i2_lower = False
            # print('i1',i1,'  i2',i2)
            if n > 0 and m > 0:
                if  (i2 >= m) or (i1 < n and nums1[i1] <= nums2[i2]):
                    i1_lower = True
                elif (i1 >= n) or (i2 < m and nums2[i2] <= nums1[i1]):
                    i2_lower = True
            elif n > 0: i1_lower = True
            elif m > 0: i2_lower = True
            cur_idx += 1

            # print('cur_idx', cur_idx)
            # print('-> v ', nums1[i1] if i1_lower else nums2[i2])
            
            if not ele1_match and ele1_idx == cur_idx:
                # print('val1', nums1[i1] if i1_lower else nums2[i2])
                val += nums1[i1] if i1_lower else nums2[i2]
                ele1_match = True
            if not ele2_match and ele2_idx == cur_idx:
                # print('val2', nums1[i1] if i1_lower else nums2[i2])
                val += nums1[i1] if i1_lower else nums2[i2]
                ele2_match = True

            if i1_lower: i1 += 1
            if i2_lower: i2 += 1
                
        return float(val) if ele2_idx == 0 else val / 2.0
                
if __name__ == '__main__':
    s = Solution()
    # a = s.findMedianSortedArrays([1,3], [2,4])
    # print('\n')
    # print(s.findMedianSortedArrays([], [1]))
    # print('\n')
    # print(s.findMedianSortedArrays([], [2,3]))
    # print('\n')
    # print(s.findMedianSortedArrays([1,3], [2,4]))
    # print('\n')
    # print(s.findMedianSortedArrays([1], [2,3,4]))
    print('\n')
    print(s.findMedianSortedArrays([1,2], [1,2]))
    # print(s.findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10]))
    # s.findMedianSortedArrays([1,3,5,7,9,11], [2,4,6,8,10,12,14])
