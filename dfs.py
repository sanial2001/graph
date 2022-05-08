vertices = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]

class Graph:
    def __init__(self, v, e):
        self.graph = [[] for _ in range(v)]
        self.visit_check = [False] * len(self.graph)
        for node1, node2 in e:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def dfs(self, source):
        visited = [False] * len(self.graph)
        stack = [source]
        dfs_list = []
        while len(stack) > 0:
            current_node = stack.pop()
            if not visited[current_node]:
                visited[current_node] = True
                dfs_list.append(current_node)
                for node in self.graph[current_node]:
                    stack.append(node)
        return dfs_list

    def display(self):
        for index, node in enumerate(self.graph):
            print('{} : {}'.format(index, node))


if __name__ == "__main__":
    graph = Graph(vertices, edges)
    graph.display()
    print(graph.dfs(0))
