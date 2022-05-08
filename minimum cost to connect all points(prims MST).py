import heapq


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        graph = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([j, dist])
                graph[j].append([i, dist])

        visited = set()
        pq = [(0, 0)]
        ans = 0
        while pq:
            dist, node = heapq.heappop(pq)
            if node in visited:
                continue
            ans += dist
            visited.add(node)
            for nei_node, nei_dist in graph[node]:
                if nei_node not in visited:
                    heapq.heappush(pq, (nei_dist, nei_node))
        return ans
