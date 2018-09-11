class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        output_str = ''
        sorted_indexes = [(i[0],i[1]) for i in sorted(enumerate(indexes), key=lambda x:x[1])]
        cur_idx = 0
        for i, idx in sorted_indexes:
            if idx != cur_idx:
                output_str += S[cur_idx:idx]
                cur_idx = idx
            dest = sources[i]
            src = None
            if idx < len(S) and len(dest)+idx <= len(S):
                src = S[idx:idx+len(dest)]

            if src == dest:
                output_str += targets[i]
            else:
                output_str += src

            if src:
                cur_idx = idx+len(src)

        if cur_idx < len(S):
            output_str += S[cur_idx:len(S)]
        return output_str
            

if __name__ == '__main__':
    s = Solution()
    # output = s.findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"])
    # assert output == 'eeebffff'
    output = s.findReplaceString(S = "abcdefghi", indexes = [1,4, 7], sources = ["bc","ef", 'h'], targets = ["eee","ffff", '999'])
    assert output == 'aeeedffffg999i'
    output = s.findReplaceString(S = "vmokgggqzp", indexes = [3,5,1], sources = ["kg","ggq","mo"], targets = ["s","so","bfr"])
    assert output == "vbfrssozp"

