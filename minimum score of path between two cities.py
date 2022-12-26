class Solution:
    def dfs(self, graph, node, visit):
        for nei, dist in graph[node]:
            self.ans = min(self.ans, dist)
            if nei not in visit:
                visit.add(nei)
                self.dfs(graph, nei, visit)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {i + 1: [] for i in range(n)}
        for u, v, val in roads:
            graph[u].append([v, val])
            graph[v].append([u, val])

        self.ans = float("inf")
        visit = set()
        visit.add(1)
        self.dfs(graph, 1, visit)
        return self.ans
