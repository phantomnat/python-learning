class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.brute_force(s)

    def brute_force(self, s):
        i = j = 0
        n = len(s)
        longest_len = 0
        longest_text = ''

        for i in range(n):
            for j in range(i, n + 1):
                if j-i <= longest_len:
                    continue
                text = s[i:j]
           
                is_palindrome = self.is_palindrome(text)
                
                if is_palindrome and len(text) > longest_len:
                    longest_len = len(text)
                    longest_text = text

        return longest_text

        
    def is_palindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome('babad'))
    # assert not s.isPalindrome('sad')
    # assert s.isPalindrome('sas')
    assert s.longestPalindrome('babad') in ['aba', 'bab']
    # assert s.longestPalindrome('cbbd') == 'bb'
    assert s.longestPalindrome('a') == 'a'
    print('ok')