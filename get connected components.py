def dfs(graph, node, path, visited):
    visited[node] = True
    path.append(node)
    for i in graph[node]:
        if visited[i] == False:
            dfs(graph, i, path, visited)


def solution(graph):
    visited = [False for _ in range(len(graph))]
    ans = []
    for i in range(len(graph)):
        if visited[i] == False:
            path = []
            dfs(graph, i, path, visited)
            ans.append(path)
    print(ans)


if __name__ == "__main__":
    graph = [[1], [0], [3], [2], [5, 6], [4, 6], [4, 5]]
    solution(graph)
