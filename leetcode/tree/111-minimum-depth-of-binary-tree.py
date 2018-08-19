# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        depth = 0

        if root is None: return depth

        current_lv = [root]
        next_lv = []

        depth = 1
        while True:
            ptr = current_lv.pop(0)

            if ptr.left is None and ptr.right is None:
                return depth
            # scan for next leafs
            if ptr.left is not None:
                next_lv.append(ptr.left)
            if ptr.right is not None:
                next_lv.append(ptr.right)
            
            if len(current_lv) == 0:
                if len(next_lv) == 0:
                    break
                # new lv
                current_lv = next_lv[:]
                next_lv = []
                depth += 1
                
        return depth