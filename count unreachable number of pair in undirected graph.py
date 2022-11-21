class Solution:
    def dfs(self, graph, node, visit):
        for nei in graph[node]:
            if nei not in visit:
                visit.add(nei)
                self.cnt += 1
                self.dfs(graph, nei, visit)

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph.items())

        sums, ans = 0, 0
        visit = set()
        for i in range(n):
            if i not in visit:
                visit.add(i)
                self.cnt = 1
                self.dfs(graph, i, visit)
                ans += sums * self.cnt
                sums += self.cnt

        return ans
