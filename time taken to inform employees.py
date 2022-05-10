class Solution:
    def dfs(self, graph, node, visit, informTime):
        ans = 0
        visit.add(node)
        for nei in graph[node]:
            if nei not in visit:
                ans = max(ans, self.dfs(graph, nei, visit, informTime) + informTime[node])
        return ans

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {i: [] for i in range(n)}
        for i, val in enumerate(manager):
            if val == -1:
                continue
            graph[i].append(val)
            graph[val].append(i)

        visit = set()
        return self.dfs(graph, headID, visit, informTime)
