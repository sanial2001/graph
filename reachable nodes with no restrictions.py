class Solution:
    def dfs(self, g, node, visit, restricted):
        # print(node)
        self.cnt += 1
        for nei in g[node]:
            if nei not in visit and nei not in restricted:
                visit.add(nei)
                self.dfs(g, nei, visit, restricted)

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = {i: [] for i in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        self.cnt = 0
        visit = set()
        visit.add(0)
        self.dfs(g, 0, visit, restricted)
        return self.cnt
