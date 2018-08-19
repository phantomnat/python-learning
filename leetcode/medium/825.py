class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = 0
        cache = {}
        
        for _, A in enumerate(ages):
            cache[A] = cache.get(A, 0) + 1
            
        k_ages = sorted(cache.keys())
        
        # k_ages.sort()
        print(k_ages)
        print(cache)
        
        for A in k_ages:
            for B in k_ages:
                if B <= 0.5 * A + 7:
                    pass
                elif B > A:
                    break
                elif A < 100 and B > 100:
                    break
                elif A == B:
                    count += (cache[A] ** 2) - cache[A]
                else:
                    count += cache[A] * cache[B]
        return count

s = Solution()
# print(s.numFriendRequests([16,16]))
print(s.numFriendRequests([1,1,1,2,2,2,3,3,3,99,99,100,100,101,101]))
