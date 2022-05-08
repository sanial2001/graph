vertices = 9
edges = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]


class Graph:
    def __init__(self, v, e):
        self.graph = [[] for _ in range(v)]
        self.visit_check = [False] * len(self.graph)
        for node1, node2 in e:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def display(self):
        for index, node in enumerate(self.graph):
            print('{} : {}'.format(index, node))

    def bfs(self, source):
        visited = [False] * len(self.graph)
        visited[source] = True
        bfs_list = [source]
        index = 0
        while index < len(bfs_list):
            for node in self.graph[bfs_list[index]]:
                if not visited[node]:
                    bfs_list.append(node)
                    self.visit_check[node] = True
                    visited[node] = True
            index = index + 1
        return bfs_list

    def connected_components(self):
        index = 0
        count = 0
        while index < len(self.graph):
            if not self.visit_check[index]:
                self.visit_check[index] = True
                print(self.bfs(index))
                count = count + 1
            index = index + 1
        print('connected components : {}'.format(count))


if __name__ == "__main__":
    graph = Graph(vertices, edges)
    print(graph.bfs(3))
    graph.connected_components()
