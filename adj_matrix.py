vertices = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]


class Graph:
    def __init__(self, v, edges):
        self.graph = [[0 for x in range(v)] for y in range(v)]
        for node1, node2 in edges:
            self.graph[node1][node2] = 1
            self.graph[node2][node1] = 1

    def display(self):
        for row in self.graph:
            print(row)


if __name__ == "__main__":
    graph = Graph(vertices, edges)
    graph.display()