class Solution:
    def iscycle(self, graph, node, visited):
        if visited[node] == 2:
            return True
        visited[node] = 2
        for i in graph[node]:
            if visited[i] != 1:
                if self.iscycle(graph, i, visited):
                    return True
        visited[node] = 1
        return False

    def canFinish(self, n: int, prerequisites) -> bool:
        graph = {i: [] for i in range(n)}
        for src, dest in prerequisites:
            graph[src].append(dest)
        visited = [0 for _ in range(n)]

        for i in range(n):
            if visited[i] == 0:
                if self.iscycle(graph, i, visited):
                    return False
        return True