vertices = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]


class Graph:
    def __init__(self, v, edges):
        self.graph = [[] for _ in range(v)]
        for node1, node2 in edges:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def __repr__(self):
        return '\n'.join(['{} : {}'.format(index, neighbors) for (index, neighbors) in enumerate(self.graph)])

    def __str__(self):
        return repr(self)


if __name__ == '__main__':
    graph = Graph(vertices, edges)
    print(str(graph))