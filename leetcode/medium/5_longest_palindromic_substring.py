class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.manacher(s)

    # def brute_force(self, s):
    #     i = j = 0
    #     n = len(s)
    #     longest_len = 0
    #     longest_text = ''
        
    #     for i in range(n):
    #         for j in range(i, n + 1):
    #             if j-i <= longest_len:
    #                 continue
    #             text = s[i:j]
           
    #             is_palindrome = self.is_palindrome(text)

    #             if is_palindrome and len(text) > longest_len:
    #                 longest_len = len(text)
    #                 longest_text = text

    #     return longest_text

    def manacher(self, s):
        c = r = 0
        
        T = '#'+'#'.join([c for c in s])+'#'
        n = len(T)
        P = [0 for x in range(n)]

        # print(T)
        max_palin_len = 0
        max_palin_idx = -1

        for i in range(1, n-1):
            # cal P[i]
            _i = 2 * c - i  # c - (i - c)

            P[i] = min([r-i, P[_i]]) if r > i else 0

            while i + 1 + P[i] < n and i - 1 - P[i] >= 0 and T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            
            # print('P[i={}]: {}'.format(i, P[i]))

            if i + P[i] > r:
                c = i
                r = i + P[i]

            if P[i] > max_palin_len:
                max_palin_len = P[i]
                max_palin_idx = i
        # print(max_palin_len, max_palisn_idx)
        n = len(s)
        # print(max_palin_idx, max_palin_len)
        if max_palin_len % 2 == 0:
            # even
            start = ((max_palin_idx // 2) - 1) - ((max_palin_len - 2) // 2)
            end = ((max_palin_idx // 2)) + ((max_palin_len - 2) // 2)
        else:
            # odd
            start = ((max_palin_idx - 1) // 2) - ((max_palin_len - 1) // 2)
            end = ((max_palin_idx - 1) // 2) + ((max_palin_len - 1) // 2)
        # print(s[start:end + 1])
        return s[start:end + 1]
    # def manacher_expand(self, s, n, i):
    #     idx = i - 1
    #     l = (idx) // 2
    #     r = l if (idx) % 2 == 0 else l + 1
        
    #     p = 0
    #     # print(i, l, r)
    #     print('i={}  s[l={}]: {}, s[r={}]: {}'.format(i, l, s[l], r, s[r]))
    #     while True:
    #         if s[l] != s[r]:
    #             print('mismatch', s[l:r+1],' p=',p * 2 if idx % 2 == 1 else (p * 2) + 1)
    #             return p * 2 if idx % 2 == 1 else (p * 2) + 1
    #         elif l - 1 < 0 or r + 1 >= n:
    #             print('out of range',s[l:r+1],' p=',p * 2 if idx % 2 == 1 else (p * 2) + 1)
    #             return p * 2 if idx % 2 == 1 else (p * 2) + 1
            
    #         l -= 1
    #         r += 1
    #         if s[l] == s[r]:
    #             p += 1
            
    def center_expand(self, s):
        n = len(s)
        i = j = 0
        ans_i = ans_j = ans_n = 0

        for center in range((2 * n) -1):
            i = center // 2
            j = (center // 2) if center % 2 == 0 else (i + 1)

            if s[i] != s[j]:
                continue

            palind_len, expand_len = self._expand(s, n, i, j)

            if s[i] == s[j] and palind_len > ans_n:
                ans_i = i - expand_len
                ans_j = j + expand_len
                ans_n = palind_len

        return s[ans_i:ans_j+1]

    def _expand(self, s, n, i, j):
        expand = 0
        while True:
            if s[i] != s[j]:
                return 0 if i == j else (j-i-1), expand - 1
            if i - 1 < 0 or j + 1 >= n:
                return j-i+1, expand
            j += 1
            i -= 1
            expand += 1

    def dp(self, s):
        ans = ''
        ans_len = 0
        n = len(s)
        dp = [[False for x in range(n)] for y in range(n)]

        print(s)
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # print(i,j)
                print('s[i={}]: {} , s[j={}]: {}'.format(i, s[i], j, s[j]))
                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1])
                if dp[i][j] and ans_len < j - i + 1:
                    ans = s[i:j+1]
                    print(ans)
                    ans_len = j - i + 1

        return ans
        
    def is_palindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome('babad'))
    # assert not s.isPalindrome('sad')
    # assert s.isPalindrome('sas')
    # assert s.longestPalindrome('babad') in ['aba', 'bab']
    # assert s.longestPalindrome('babab') == 'babab'
    # assert s.longestPalindrome('aaaa') == 'aaaa'
    # assert s.longestPalindrome('abbc') == 'bb'
    # assert s.longestPalindrome('abddbc') == 'bddb'
    # assert s.longestPalindrome('aaaaaaaaaaaaaa') == 'aaaaaaaaaaaaaa'
    # print(s.longestPalindrome("babcbabcbaccba"))
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("abaaba") == "abaaba"
    assert s.longestPalindrome("aaabaaaa") == "aaabaaa"
    assert s.longestPalindrome('cbbd') == 'bb'
    assert s.longestPalindrome('a') == 'a'
    print('ok')