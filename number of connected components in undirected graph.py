def dfs(graph, node, visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, edges):
    graph = {i: [] for i in range(n)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if not visited[i]:
            ans += 1
            dfs(graph, i, visited)
    print(ans)


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    solution(n, edges)
