import collections


class Solution:
    def dfs(self, graph, node, visit):
        self.ch = min(self.ch, node)
        visit.add(node)
        for nei in graph[node]:
            if nei not in visit:
                self.dfs(graph, nei, visit)

    def solve(self, a, b, target):
        n = len(a)
        graph = collections.defaultdict(set)
        for i in range(n):
            graph[a[i]].add(b[i])
            graph[b[i]].add(a[i])

        res = ''
        dp = collections.defaultdict(str)
        for i in range(len(target)):
            if target[i] in dp:
                res += dp[target[i]]
            elif target[i] in graph:
                visit = set()
                self.ch = 'z'
                self.dfs(graph, target[i], visit)
                res += self.ch
                dp[target[i]] = self.ch
            else:
                res += target[i]
                dp[target[i]] = target[i]

        return res
