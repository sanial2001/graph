class Solution:
    def cycle(self, graph, visit, node, mp):
        # print(visit)
        if visit[node] == 2:
            # print(node, self.cnt)
            self.cnt = self.cnt - mp[node]
            return True
        visit[node] = 2
        mp[node] = self.cnt
        for nei in graph[node]:
            if visit[nei] != 1:
                self.cnt += 1
                if self.cycle(graph, visit, nei, mp):
                    return True
        visit[node] = 1
        return False

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = {i: [] for i in range(n)}
        for u, v in enumerate(edges):
            if v != -1:
                graph[u].append(v)

        res = -1
        visit = [0] * n
        for i in range(n):
            if visit[i] == 0:
                self.cnt = 0
                mp = {i: 0 for i in range(n)}
                if self.cycle(graph, visit, i, mp):
                    res = max(res, self.cnt)

        return res
