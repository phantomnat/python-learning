class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' ',
        }
        
        if len(digits) == 0:
            return []

        ans = [x for x in phone[digits[0]]]
 
        for d in range(1, len(digits)):
            ans = [''.join([y,x]) for x in phone[digits[d]] for y in ans]
        return ans
            

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations("232"))

    # print(s.letterCombinations([-1,0,1,2,-1,-4]))