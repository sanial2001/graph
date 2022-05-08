import heapq


class Solution:
    def swimInWater(self, grid) -> int:
        n = len(grid)
        minheap = [(grid[0][0], 0, 0)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True

        while minheap:
            maxht, x, y = heapq.heappop(minheap)
            # print(maxht, x, y)
            if x == n - 1 and y == n - 1:
                return maxht
            if x > 0 and visited[x - 1][y] == False:
                visited[x - 1][y] = True
                heapq.heappush(minheap, (max(maxht, grid[x - 1][y]), x - 1, y))
            if y > 0 and visited[x][y - 1] == False:
                visited[x][y - 1] = True
                heapq.heappush(minheap, (max(maxht, grid[x][y - 1]), x, y - 1))
            if x < n - 1 and visited[x + 1][y] == False:
                visited[x + 1][y] = True
                heapq.heappush(minheap, (max(maxht, grid[x + 1][y]), x + 1, y))
            if y < n - 1 and visited[x][y + 1] == False:
                visited[x][y + 1] = True
                heapq.heappush(minheap, (max(maxht, grid[x][y + 1]), x, y + 1))
