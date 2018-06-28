class Solution(object):
    def pruneTree(self, root):
        def checkit (root):
            if not root:
                return False
            if root.val == 1:
                return True 
            return checkit(root.left) or checkit(root.right)
        def cut(root):
            if  checkit(root) == False:
                return None
            else:
                root.left = cut(root.left)
                root.right = cut(root.right)
                return root
        return cut(root)
   