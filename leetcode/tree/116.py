# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# tree


# Definition for a Node.
class Node:
    def __init__(self, val, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bfs
        search = [root]
        next_search = []
        while len(search) > 0:
            p, search = search[0], search[1:]
            if p.left: next_search.append(p.left)
            if p.right: next_search.append(p.right)
            if len(search) > 0:
                p.next = search[0]
            if len(search) == 0 and len(next_search) > 0:
                search = next_search
                next_search = []
        
        return root

if __name__ == '__main__':
    s = Solution()
    lv2_1l, lv2_1r = Node(4), Node(5)
    lv2l_1r, lv2r_1r = Node(6), Node(7)
    lv1l, lv1r = Node(2, lv2_1l, lv2_1r), Node(3, lv2_1l, lv2_1r)
    root = Node(1, lv1l, lv1r)
    s.connect(root)
    print(root)