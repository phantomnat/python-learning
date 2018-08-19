# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        cache = {0:1}
        self.dfs(root, sum, cache, 0)
        return self.result

    def dfs(self, root, target, cache, curPath = 0):
        if root is None:
            return 
        curPath += root.val
        oldPath = curPath - target

        self.result += cache.get(oldPath, 0)
        cache[curPath] += cache.get(curPath, 0) + 1

        self.dfs(root.left, target, cache, curPath)
        self.dfs(root.right, target, cache, curPath)

        cache[curPath] -= 1
        
    # def dfs(self, root_map, node, target, total=0, path=[], result=[]):
    #     if node is None:
    #         return

    #     # print(' target {} = {} + {}  {}'.format(target, total, node.val, path+[node.val]))
    #     if target == total + node.val:
    #         result.append(path+[node.val])
        
    #     # search with root
    #     # if node.left is not None:
    #     # if node.right is not None:
    #     self.dfs(root_map, node.left, target, total + node.val, path+[node.val], result)
    #     if node.left not in root_map:
    #         root_map[node.left] = True
    #         self.dfs(root_map, node.left, target, 0, [], result)

    #     self.dfs(root_map, node.right, target, total + node.val, path+[node.val], result)
    #     if node.right not in root_map:
    #         root_map[node.right] = True
    #         self.dfs(root_map, node.right, target, 0, [], result)


#          1
#        /   \
#    -2        -3
#    /\        |
#   1  3     -2
#  /
#-1

# [10,
# 5,-3,
# 3,2,None,11,
# 3,-2,None,1]

s = Solution()

# root = TreeNode(10)

# root.left = TreeNode(5)
# root.right = TreeNode(-3)

# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.left = None
# root.right.right = TreeNode(11)

# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# # root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(1)

# print(s.pathSum(root, 8))

# def build_tree(root, arr):
# [1,-2,-3,1,3,-2,None,-1]

# root = TreeNode(1)

# root.left = TreeNode(-2)
# root.right = TreeNode(-3)

# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(-2)
# root.right.right = None

# root.left.left.left = TreeNode(-1)

# print(s.pathSum(root, 3))
# def build_tree(arr):
#     root = TreeNode(0)
#     ptr = root
#     for i in range(1, len(arr)):
#         if i % 2 == 1:
#             ptr.left = TreeNode(0)
#             ptr = ptr.left
#     return root

# root = TreeNode(0)
# root.left = TreeNode(0)
# root.left.left = TreeNode(0)
# root.left.left.left = TreeNode(0)
# root.left.left.left.left = TreeNode(0)
# root.left.left.left.left.left = TreeNode(0)


# q =[0,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0,None,0]

# print(s.pathSum(build_tree(q), 0))
