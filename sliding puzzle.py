class Solution:
    def swap(self, s, i, j):
        l = list(s)
        l[i], l[j] = l[j], l[i]
        return ''.join(l)

    def slidingPuzzle(self, board) -> int:
        swap = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [3, 1, 5], [2, 4]]
        first = ""
        for i in range(2):
            for j in range(3):
                first += str(board[i][j])

        pq = [first]
        visited = set()
        visited.add(first)
        ans = 0
        while pq:
            for i in range(len(pq)):
                item = pq.pop(0)
                if item == "123450":
                    return ans
                index = item.index("0")
                for val in swap[index]:
                    candidate = self.swap(item, index, val)
                    if candidate not in visited:
                        visited.add(candidate)
                        pq.append(candidate)
            ans += 1
        return -1
