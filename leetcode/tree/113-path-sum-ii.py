# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root, _sum, 0, [], result)
        return result

    def dfs(self, node, target, total=0, path=[], result=[]):
        if node is None:
            return False

        if node.left is None and node.right is None and target == total + node.val:
            result.append(path+[node.val])
            return
        
        self.dfs(node.left, target, total + node.val, path+[node.val], result)
        self.dfs(node.right, target, total + node.val, path+[node.val], result)
