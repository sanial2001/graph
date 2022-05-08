class Solution:
    def dfs(self, graph, node, path, ans):
        if node == len(graph) - 1:
            ans.append(path[::])
            return
        for i in graph[node]:
            path.append(i)
            self.dfs(graph, i, path, ans)
            path.pop()

    def allPathsSourceTarget(self, graph):
        path, ans = [0], []
        self.dfs(graph, 0, path, ans)
        return ans
