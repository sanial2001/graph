class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        visit.add((0, 0, 0))
        q = [[0, 0, 0, 0]]

        while q:
            x, y, obstacle, path = q.pop(0)

            if x == m - 1 and y == n - 1:
                return path

            if x > 0:
                if grid[x - 1][y] == 1 and obstacle < k and (x - 1, y, obstacle + 1) not in visit:
                    visit.add((x - 1, y, obstacle + 1))
                    q.append([x - 1, y, obstacle + 1, path + 1])
                elif grid[x - 1][y] == 0 and (x - 1, y, obstacle) not in visit:
                    visit.add((x - 1, y, obstacle))
                    q.append([x - 1, y, obstacle, path + 1])

            if y > 0:
                if grid[x][y - 1] == 1 and obstacle < k and (x, y - 1, obstacle + 1) not in visit:
                    visit.add((x, y - 1, obstacle + 1))
                    q.append([x, y - 1, obstacle + 1, path + 1])
                elif grid[x][y - 1] == 0 and (x, y - 1, obstacle) not in visit:
                    visit.add((x, y - 1, obstacle))
                    q.append([x, y - 1, obstacle, path + 1])

            if x < m - 1:
                if grid[x + 1][y] == 1 and obstacle < k and (x + 1, y, obstacle + 1) not in visit:
                    visit.add((x + 1, y, obstacle + 1))
                    q.append([x + 1, y, obstacle + 1, path + 1])
                elif grid[x + 1][y] == 0 and (x + 1, y, obstacle) not in visit:
                    visit.add((x + 1, y, obstacle))
                    q.append([x + 1, y, obstacle, path + 1])

            if y < n - 1:
                if grid[x][y + 1] == 1 and obstacle < k and (x, y + 1, obstacle + 1) not in visit:
                    visit.add((x, y + 1, obstacle + 1))
                    q.append([x, y + 1, obstacle + 1, path + 1])
                elif grid[x][y + 1] == 0 and (x, y + 1, obstacle) not in visit:
                    visit.add((x, y + 1, obstacle))
                    q.append([x, y + 1, obstacle, path + 1])

        return -1
