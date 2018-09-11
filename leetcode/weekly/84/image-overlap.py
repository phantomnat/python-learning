import collections
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        LA = [i // N * 100 + i % N for i in range(N * N) if A[i // N][i % N]]
        LB = [i // N * 100 + i % N for i in range(N * N) if B[i // N][i % N]]
        c = collections.Counter(i - j for i in LA for j in LB)
        print(LA)
        print(LB)

if __name__ == '__main__':
    s = Solution()
    out = s.largestOverlap(A = [[1,1,0],
            [0,1,0],
            [0,1,0]], B = [[0,0,0],
            [0,1,1],
            [0,0,1]])