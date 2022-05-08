class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        t = [float("inf") for i in range(n)]
        t[src] = 0
        for i in range(k + 1):
            temp = t[::]
            for src, dest, price in flights:
                if t[src] == float("inf"):
                    continue
                if t[src] + price < temp[dest]:
                    temp[dest] = t[src] + price
            t = temp
        return -1 if t[dst] == float("inf") else t[dst]
