# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        current_lv = [root]
        next_lv = []

        result = []
        result_per_lv = []
        if root is None: return []
        while True:
            ptr = current_lv.pop(0)

            result_per_lv.append(ptr.val)

            # scan for next leafs
            if ptr.left is not None:
                next_lv.append(ptr.left)
            if ptr.right is not None:
                next_lv.append(ptr.right)
            
            if len(current_lv) == 0:
                result.append(result_per_lv)
                if len(next_lv) == 0:
                    break
                # new lv
                current_lv = next_lv[:]
                next_lv = []
                result_per_lv = []
                
        return result