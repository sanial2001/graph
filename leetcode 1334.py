from collections import defaultdict
from heapq import heappush, heappop


def findTheCity(N, edges, distThre):
    G = defaultdict(list)
    for u, v, w in edges:
        G[u].append([v, w])
        G[v].append([u, w])

    def dijkstra(i):
        pq = []
        heappush(pq, [0, i])
        path = [float("inf")] * N
        path[i] = 0

        while pq:
            dist, node = heappop(pq)
            if dist > distThre:
                break
            for nei, w in G[node]:
                if dist + w < path[nei]:
                    path[nei] = dist + w
                    heappush(pq, [path[nei], nei])

        cnt = -1
        for i in range(N):
            cnt += path[i] <= distThre
        return cnt

    cnts = {}
    mini, maxi = N + 1, 0
    for i in range(N):
        cnts[i] = dijkstra(i)
        mini = min(cnts[i], mini)
        if cnts[i] == mini:
            maxi = max(maxi, i)
    return maxi


def solve(distanceThreshold, city_nodes, city_from, city_to, city_weight):
    edges = []
    for i in range(len(city_from)):
        edges.append([city_from[i] - 1, city_to[i] - 1, city_weight[i]])
    return findTheCity(city_nodes, edges, distanceThreshold) + 1
