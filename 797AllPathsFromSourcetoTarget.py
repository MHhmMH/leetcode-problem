class Solution(object):
    #DfS using stack
    def allPathsSourceTarget(self, graph):
        stack = [(0,[0])]
        res = []
        while stack:
            node, path = stack.pop()
            if node == len(graph)- 1:
                res.append(path)
            for neigh in graph[node]:
                stack.append((neigh, path + [neigh]))
        return res
    #Recursively traverse the graph:
    def allPathsSourceTarget(self, graph):
        def move(node,pathnow):
            if node == len(graph)-1:
                res.append(pathnow)
            for node in graph[node]:
                move(node, pathnow+[node])
        res = [ ] 
        move(0,[0])
        return res