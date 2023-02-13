import collections
import heapq

graph_list = collections.defaultdict(list)
res = []


def create_graph(V, E, edges):
    # Set up and print the adjacency matrix representation of the graph.
    graph = [[[0, 0] for _ in range(V)] for _ in range(V)]
    for u, v, w in edges:
        graph[u - 1][v - 1] = [1, w]
        graph[v - 1][u - 1] = [1, w]
        graph_list[u].append([v, w])
        graph_list[v].append([u, w])

    for edges in graph:
        print(edges)
    #print(graph_list)

    return graph


def dfs(node, visit, res):
    # Recursive function to iterate through the graph
    for nei, weight in graph_list[node]:
        if nei not in visit:
            res.append(nei)
            visit.add(nei)
            dfs(nei, visit, res)


def connected_components(n):
    # Determine how many components the graph has and print each component in adjacency list representation
    count, ans = 0, []
    visit = set()
    for node in range(1, n + 1):
        res = []
        if node not in visit:
            count += 1
            res = [node]
            visit.add(node)
            dfs(node, visit, res)
        if res: ans.append(res)
    print(count, ans)


def mst(node):
    # minimum spanning tree for every connected node of the graph
    visited = set()
    pq = [(0, node)]
    ans = 0
    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited:
            continue
        ans += dist
        visited.add(node)
        for nei_node, nei_dist in graph_list[node]:
            if nei_node not in visited:
                heapq.heappush(pq, (nei_dist, nei_node))
    return ans


def connected_components_for_mst(n):
    ans = []
    visit = set()
    for node in range(1, n + 1):
        res = []
        if node not in visit:
            res = [node]
            visit.add(node)
            dfs(node, visit, res)
            min_dist = mst(node)
        if res: ans.append([res, min_dist])
    print(ans)


if __name__ == "__main__":
    # Read in the number of vertices V and the number of edges E of the graph followed by its E edges, each in the form u, v, w where I <= u, v < V & W > 0 representing an edge uv with weight w.
    print("Enter the number of vertices : ")
    V = int(input())
    print("Enter the number of edges : ")
    E = int(input())
    print("Enter the edges with spaced input followed by new line")
    edges = []
    for i in range(E):
        u, v, w = list(map(float, input().split()))
        u, v = int(u), int(v)
        edges.append([u, v, w])
    Graph = create_graph(V, E, edges)
    connected_components(V)
    connected_components_for_mst(V)

    '''
    Graph = create_graph(4, 3, [[1, 2, 0.98], [1, 3, 3.22], [2, 4, 1.33]])
    connected_components(4)
    connected_components_for_mst(4)
    '''