class Solution:
    def nearestExit(self, maze, entrance) -> int:
        '''
        for val in maze:
            print(val)
        '''
        m, n = len(maze), len(maze[0])
        q, ans = [entrance], 0
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            num = len(q)
            for i in range(num):
                x, y = q[0]
                if (x == 0 or y == 0 or x == m - 1 or y == n - 1) and ans > 0:
                    return ans
                q.pop(0)
                if x > 0 and maze[x - 1][y] == '.':
                    maze[x - 1][y] = '+'
                    q.append([x - 1, y])
                if y > 0 and maze[x][y - 1] == '.':
                    maze[x][y - 1] = '+'
                    q.append([x, y - 1])
                if x < m - 1 and maze[x + 1][y] == '.':
                    maze[x + 1][y] = '+'
                    q.append([x + 1, y])
                if y < n - 1 and maze[x][y + 1] == '.':
                    maze[x][y + 1] = '+'
                    q.append([x, y + 1])
            ans += 1

        return -1
