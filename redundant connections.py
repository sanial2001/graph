class Solution:
    def dfs(self, graph, src, dest, visited):
        if src == dest:
            return True
        visited[src] = True
        for nei in graph[src]:
            if visited[nei] == False:
                if self.dfs(graph, nei, dest, visited):
                    return True
        return False

    def findRedundantConnection(self, edges):
        n = len(edges)
        graph = {i + 1: [] for i in range(n)}
        for edge in edges:
            src, dest = edge
            if src in graph and dest in graph and self.dfs(graph, src, dest, [False] * (n + 1)):
                return edge
            graph[src].append(dest)
            graph[dest].append(src)
