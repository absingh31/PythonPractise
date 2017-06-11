# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None

        map = {}

        q = [node]

        newrootnode = UndirectedGraphNode(node.label)
        map[node] = newrootnode

        while len(q):
            u = q.pop(0)

            for ne in u.neighbors:
                if ne not in map:
                    newnode = UndirectedGraphNode(ne.label)
                    map[u].neighbors.append(newnode)
                    map[ne] = newnode
                    q.append(ne)
                else:
                    map[u].neighbors.append(map[ne])

        return newrootnode

