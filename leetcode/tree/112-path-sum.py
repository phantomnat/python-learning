# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, node, target, total=0):
        if node is None:
            return False

        # if abs(total) > abs(target) or abs(node.val + total) > abs(target):
        #     return False

        if node.left is None and node.right is None and target == total + node.val:
            return True
        
        l = False if node.left is None else self.dfs(node.left, target, total + node.val)
        r = False if node.right is None else self.dfs(node.right, target, total + node.val)

        return l or r
            
    def hasPathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, _sum, 0)

# s = Solution()
# root = TreeNode(-2)
# root.right = TreeNode(-3)
# print(s.hasPathSum(root, -5))

# root = TreeNode(8)
# root.left = TreeNode(9)
# root.right = TreeNode(-6)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(9)
# print(s.hasPathSum(root, 7))