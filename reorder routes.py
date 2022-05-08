class Solution:
    def minReorder(self, n: int, connections) -> int:
        graph = {i: [] for i in range(n)}
        for src, dest in connections:
            graph[src].append([dest, 1])
            graph[dest].append([src, 0])
        # print(graph)
        visited = [False for _ in range(n)]
        q, ans = [0], 0

        while q:
            node = q.pop(0)
            visited[node] = True
            for nei, cost in graph[node]:
                if visited[nei] == False:
                    ans += cost
                    q.append(nei)

        return ans
