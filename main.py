vertices = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]


class Graph:
    def __init__(self, v, e):
        self.graph = [[] for _ in range(v)]
        for node1, node2 in e:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def check(self):
        visited = [False] * len(self.graph)
        visited[3] = True
        for i in self.graph[3]:
            print(i, 'hello')


if __name__ == "__main__":
    graph = Graph(vertices, edges)
    graph.check()
