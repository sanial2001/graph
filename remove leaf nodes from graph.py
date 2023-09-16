import collections


def solve(N, edges):
    graph = {i: [] for i in range(N)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # print(graph.items())

    leaves = []
    for node in graph:
        if len(graph[node]) <= 1:
            leaves.append(node)

    steps = 0
    while len(leaves) > 0:
        # print(leaves)
        new_leaves = []
        for leaf in leaves:
            if len(graph[leaf]) == 0:
                continue
            nei = graph[leaf].pop()
            del graph[leaf]
            graph[nei].remove(leaf)
            if len(graph[nei]) == 1:
                new_leaves.append(nei)
        leaves = new_leaves
        steps += 1

    return steps


def func(N, A, B):
    n = len(A)
    edges = []
    for i in range(n):
        edges.append([A[i], B[i]])
    return solve(N, edges)


if __name__ == "__main__":
    print(func(4, [0, 1, 2], [1, 2, 0]))
