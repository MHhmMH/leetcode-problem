# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
    ## this is for the case k = 0 
        if K is 0:
            return [target.val]
        graph = {}
    ## first build a graph and then use BFS to find all the nodes with distance k to the target
    ## build the gragh using the dictionary and DFS
        def buildgraph(node,parent = None):
            graph[node.val] = set()
            if parent:
                graph[node.val].add(parent.val)
            if node.left:
                graph[node.val].add(node.left.val)
                buildgraph(node.left,node)
            if node.right:
                graph[node.val].add(node.right.val)
                buildgraph(node.right,node)   
        buildgraph(root)
        visitednode = set()
        visitednode.add(target.val)
        queue = collections.deque()
        queue.append(target.val)
        k = 1
        res = []
      ## BFS to find the solution 
      ## use deque 
        while queue:
                size = len(queue)
                for i in range(size):
                    node = queue.pop()
                    for child in graph[node]:
                        if child not in visitednode:
                            queue.appendleft(child)
                            visitednode.add(child)
                        else:
                            pass
                if k  == K:
                    res = list(queue)
                    break;
                k += 1 
        return res