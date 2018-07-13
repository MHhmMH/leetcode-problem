# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sumnow = 0
        self.dfs(root)
        return root
    def dfs(self,root):
        if not root:
            return 
        self.dfs(root.right)
        root.val += self.sumnow
        self.sumnow = root.val 
        self.dfs(root.left)