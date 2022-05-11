class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = []
        n = len(graph)
        for i in range(n):
            visit = set()
            visit.add(i)
            q.append([i, visit])

        steps = 0
        while q:
            num = len(q)
            for i in range(num):
                node, visit = q.pop(0)
                # print(node, visit)
                if len(visit) == n:
                    return steps
                for nei in graph[node]:
                    temp = visit.copy()
                    temp.add(nei)
                    q.append([nei, temp])
            if q: steps += 1
