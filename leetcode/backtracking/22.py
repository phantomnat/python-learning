class Solution:
    def generateParenthesis(self, n):
        N = n
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        # backtrack()
        # self.gen(ans, n, [])
        self.backtrack(ans, n)
        # for i in range()
        return ans

    def backtrack(self, ans, n, txt = '', l = 0, r = 0):
        if len(txt) == n * 2:
            ans.append(txt)
            return
        if l < n:
            self.backtrack(ans, n, txt+'(', l+1, r)
        # if r < n and l >= r + 1:
        if r < l:
            self.backtrack(ans, n, txt+')', l, r+1)
        
    def valid(self, s):
        b = 0
        for i in s:
            b = b+1 if i == '(' else b-1
            if b < 0: return False
        return b == 0

    def gen(self, ans, n, txt = []):
        # print('gen', txt, n, len(txt))
        # if on == 1:
        # for i in range(on):
        #     txt = ' ' 
        #     for j in range(cn):
                
        if len(txt) == n * 2:
            if self.valid(txt):
                ans.append(''.join(txt))
        else:
            txt.append('(')
            self.gen(ans, n, txt)
            txt.pop()
            txt.append(')')
            self.gen(ans, n, txt)
            txt.pop()
            
            
        # if n == 2:
        #     return 
        
        # l = []
        # idx = n // 2
        
        # if n == 4:
        #     for i in range(idx):
        #         l.append(self.gen(2) + self.gen(2))
        #     return l
            
        # elif n == 4:
        #     result = []
        #     for i in range(n):
                
        # else:
        #     return 
        # for i in range(n):
        #     return '('
        #     # return '(self.gen(n-1)
        # return s


if __name__ == '__main__':
    s = Solution()
    # print(s.generateParenthesis(1))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))