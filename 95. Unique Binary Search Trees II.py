       if n == 0:
            return []
        def gettree(first,last): 
            ans = []
            for rootvalue in range(first,last + 1):
                for leftchild in gettree(first,rootvalue - 1):
                    for rightchild in gettree(rootvalue + 1,last):
                        root = TreeNode(rootvalue)
                        root.left,root.right = leftchild, rightchild
                        ans.append(root)
            return ans or [None]
        return gettree(1,n)