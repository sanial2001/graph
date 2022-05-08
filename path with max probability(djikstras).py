import heapq


class Solution:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        graph = {i: [] for i in range(n)}
        for i, edge in enumerate(edges):
            graph[edge[0]].append([edge[1], succProb[i] * (-1)])
            graph[edge[1]].append([edge[0], succProb[i] * (-1)])

        minheap = [(-1, start)]
        visit = [False for _ in range(n)]
        while minheap:
            prob, node = heapq.heappop(minheap)
            if node == end:
                return prob * -1
            visit[node] = True
            for nei, nei_prob in graph[node]:
                # print(nei_prob, nei)
                if visit[nei] == False:
                    heapq.heappush(minheap, (prob * nei_prob * -1, nei))
        return 0
