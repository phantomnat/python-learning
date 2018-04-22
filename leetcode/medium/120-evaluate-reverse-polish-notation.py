class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []

        while len(tokens) > 0:
            t = tokens.pop(0)
            if t in ['+','-','*','/']:
                a = num_stack.pop(0)
                b = num_stack.pop(0)
                if t == '+': c = a + b
                elif t == '-': c = b - a
                elif t == '*': c = a * b
                else: 
                    neg_a = 1 if a >= 0 else -1
                    neg_b = 1 if b >= 0 else -1
                    a = a if a >= 0 else -a
                    b = b if b >= 0 else -b
                    c = (b // a) * neg_a * neg_b
                num_stack.insert(0, c)
            else:
                # num
                num_stack.insert(0, int(t))
        
        return num_stack.pop(0)

if __name__ == '__main__':
    s = Solution()
    # assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    # assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22