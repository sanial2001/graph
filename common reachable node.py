class Solution:
    def dfs(self, g, node, seen):
        if node in seen:
            return
        seen.add(node)
        for nei in g[node]:
            self.dfs(g, nei, seen)

    def solve(self, edges, a, b):
        g = collections.defaultdict(list)
        for u, v in edges:
            g[v].append(u)

        s1, s2 = set(), set()
        self.dfs(g, a, s1)
        self.dfs(g, b, s2)
        # print(s1.intersection(s2))
        return True if s1.intersection(s2) else False
