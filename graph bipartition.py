class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        graph = {i + 1: [] for i in range(n)}
        for num, val in dislikes:
            graph[num].append(val)
            graph[val].append(num)
        # print(graph)

        color = [-1 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if color[i] == -1:
                color[i] = 1
                q = [i]
                while q:
                    cur = q.pop(0)
                    cur_color = color[cur]
                    for val in graph[cur]:
                        if color[val] == -1:
                            color[val] = 1 - cur_color
                            q.append(val)
                        elif color[val] == cur_color:
                            return False
        return True
