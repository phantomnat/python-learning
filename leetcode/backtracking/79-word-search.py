class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # convert to string
        # _1dTxt = ''
        if len(board) == 0:
            print('board length = 0')
            return False
        if len(word) == 0:
            print('word length = 0')
            return False

        self.height = len(board)
        self.width = len(board[0])

        id_used_map = {}

        for y, row in enumerate(board):
            for x, c in enumerate(row):
                if c == word[0] and \
                    self.search(board, word, id_used_map, (y, x)):
                    return True
            
        return False

    def search(self, board, word, id_used_map, check_pos):
        c = word[0]
        y, x = check_pos
        _id = ((y * self.width) + x)
        
        if board[y][x] != c:
            return False

        if len(word) == 1:
            return True
        
        id_used_map[_id] = True

        # upper check
        if y-1 >= 0 and (((y-1) * self.width) + x) not in id_used_map:
            if self.search(board, word[1:], id_used_map, (y-1, x)):
                return True

        # lower
        if y+1< self.height and (((y+1) * self.width) + x) not in id_used_map:
            if self.search(board, word[1:], id_used_map, (y+1, x)):
                return True
        
        # left
        if x-1 >= 0 and ((y * self.width) + x-1) not in id_used_map:
            if self.search(board, word[1:], id_used_map, (y, x-1)):
                return True

        # right
        if x+1 < self.width and ((y * self.width) + x+1) not in id_used_map:
            if self.search(board, word[1:], id_used_map, (y, x+1)):
                return True

        del id_used_map[_id]

        return False

if __name__ == '__main__':
    s = Solution()
    result = s.exist([
        ['A']
    ], "B")

    result = s.exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], "ABCCED")

    assert result, "ABCCED should be exist"

    assert s.exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], "SEE")

    assert not s.exist([
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ], "ABCB"), "ACBC should not valid"
