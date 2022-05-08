class Solution:
    def iscycle(self, graph, node, cycle):
        if cycle[node] == 2:
            return True
        cycle[node] = 2
        for i in graph[node]:
            if cycle[i] != 1:
                if self.iscycle(graph, i, cycle):
                    return True
        cycle[node] = 1
        return False

    def dfs(self, graph, node, visited, ans):
        visited[node] = True
        for i in graph[node]:
            if visited[i] == False:
                self.dfs(graph, i, visited, ans)
        ans.append(node)

    def findOrder(self, n: int, prerequisites):
        graph = {i: [] for i in range(n)}
        for val in prerequisites:
            graph[val[0]].append(val[1])
        visited = [False for _ in range(n)]
        cycle = [0 for _ in range(n)]
        for i in range(n):
            if cycle[i] == 0:
                if self.iscycle(graph, i, cycle):
                    return []
        ans = []
        for i in range(n):
            if visited[i] == False:
                self.dfs(graph, i, visited, ans)
        return ans
