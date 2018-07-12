# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def findTarget(self, root, k):
    #     """
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: bool
    #     """
    #     twosum = self.preorder(root)
    #     for i in range(len(twosum)):
    #         for j in range(i+1,len(twosum)):
    #             if twosum[i] + twosum[j] == k:
    #                 return True
    #     return False
    # def preorder(self,root):
    #     if not root:
    #         return []
    #     return self.preorder(root.left) +  [root.val] + self.preorder(root.right)
    def findTarget(self,root,k):
            if not root:
                return False
            return self.find(root,set(),k)
    def find(self,root,nodeset,k):
        if not root:
            return False
        value = k - root.val
        if value in nodeset:
            return True
        nodeset.add(root.val)
        return self.find(root.left,nodeset,k) or self.find(root.right,nodeset,k)