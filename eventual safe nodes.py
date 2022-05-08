class Solution:
    def dfs(self, graph, node, visited):
        if visited[node] == 2:
            return True
        visited[node] = 2
        for nei in graph[node]:
            if visited[nei] != 1:
                if self.dfs(graph, nei, visited) == True:
                    return True
        visited[node] = 1
        return False

    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited = [0 for _ in range(n)]
        for i in range(n):
            if visited[i] == 0:
                if self.dfs(graph, i, visited):
                    continue
        ans = []
        for i in range(n):
            if visited[i] == 1:
                ans.append(i)
        return ans
