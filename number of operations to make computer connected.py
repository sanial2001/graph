class Solution:
    def dfs(self, graph, node, visited):
        visited[node] = True
        for nei in graph[node]:
            if visited[nei] == False:
                self.dfs(graph, nei, visited)

    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1
        graph = {i: [] for i in range(n)}
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        visited = [False for _ in range(n)]
        ans = 0
        for i in range(n):
            if visited[i] == False:
                self.dfs(graph, i, visited)
                ans += 1

        return ans - 1
