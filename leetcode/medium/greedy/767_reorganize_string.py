import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:

        # greedy with heap

        pq = [(-S.count(x), x) for x in set(S)]
        print(pq)
        heapq.heapify(pq)
        print(pq)
        if any(-nc > (len(S)+1)/2 for nc,x in pq):
            return ""
        
        ans = []
        while len(pq) >= 2:
            n1, c1 = heapq.heappop(pq)
            n2, c2 = heapq.heappop(pq)
            ans.extend([c1,c2])
            if n1+1: heapq.heappush(pq, (n1+1, c1))
            if n2+1: heapq.heappush(pq, (n2+1, c2))
            print(pq)

        return ''.join(ans) + (pq[0][1] if pq else '')


        # solution

        # N = len(S)
        # A = []
        # l = sorted((S.count(x),x) for x in set(S))
        # print(l)
        # for c, x in l:
        #     if c > (N+1)/2: return ""
        #     A.extend(c * x)
        #     print('A', A)
        # ans = [''] * N
        # # ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        # ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        # print(ans)
        # return ''.join(ans)


        # my

        # mem = {}
        # N = len(S)
        # for c in S:
        #     mem[c] = mem.get(c, 0) + 1
        # print(sorted((S.count(x), x) for x in set(S)))
        # def sortByValue(v):
        #     return (v[1],v[0])
        # meml = sorted([(k,v) for k,v in mem.items()], key=sortByValue, reverse=True)
        # print(meml)
        # maxC = meml[0][1]
        # if (N%2 == 0 and maxC > N/2) or (N%2 == 1 and maxC > (N/2)+1):
        #     return ""
        # ans = [''] * N
        # i = 0
        # for (c,v) in meml:
        #     for _ in range(v):
        #         ans[i] = c
        #         i += 2
        #         if i >= N:
        #             i = 1
        # print(ans)
        # return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    # print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
    print(s.reorganizeString("aab"))    # "aba"
    print(s.reorganizeString("caaab"))   # ""
