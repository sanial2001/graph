import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = {i + 1: [] for i in range(n)}
        for src, dest, time in times:
            graph[src].append([dest, time])
        # print(graph.items())

        pq = [[0, k]]
        visited = [False for _ in range(n + 1)]
        ans = 0
        while pq:
            time, node = heapq.heappop(pq)
            if visited[node] == True:
                continue
            visited[node] = True
            ans = max(ans, time)
            for nei, nei_time in graph[node]:
                if visited[nei] == False:
                    heapq.heappush(pq, [time + nei_time, nei])

        return -1 if False in visited[1:] else ans
