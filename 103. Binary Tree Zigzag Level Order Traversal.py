# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        stack = [root] 
        rootlist = [root] 
        res = []
        level = 1 
        while stack:
            stack = []
            for node in rootlist:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            levellist = [root.val for root in rootlist]
            if level % 2 == 0:
                levellist.reverse()
            res.append(levellist)
            level += 1
            rootlist = stack
        return res