# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        currentlevel = [root]
        nextlevel = []
        res = []
        while currentlevel:
            for node in currentlevel:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            res.append(sum([node.val for node in currentlevel]) / (len(currentlevel) * 1.0))
            currentlevel = nextlevel
            nextlevel = []
        return res