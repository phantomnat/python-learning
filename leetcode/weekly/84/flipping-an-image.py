class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped = []
        for a in A:
            flipped.append(a[::-1])
        print(flipped)
        inverted = []
        for row in flipped:
            inverted.append([0 if x == 1 else 1 for x in row])
        return inverted
if __name__ == '__main__':
    s = Solution()
    output = s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
    assert output == [[1,0,0],[0,1,0],[1,1,1]]