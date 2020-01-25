# https://leetcode.com/problems/longest-palindromic-subsequence/
# medium

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # texts = list(s)
        n = len(s)
        mem = [[0] * n for _ in range(n)]

        for i in range(n):
            mem[i][i] = 1
            for j in range(i-1,-1,-1):
                if s[i] == s[j]:
                    mem[i][j] = mem[i-1][j+1] + 2
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j+1])
        
        return mem[n-1][0]

s = Solution()
print(s.longestPalindromeSubseq("dcaabbabacd"))
print(s.longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))