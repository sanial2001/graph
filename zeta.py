class Solution:
    def solve(self, start, end):
        if start > end:
            return 0
        ans = float("inf")
        for i in range(start, end + 1):
            cost1 = self.solve(start, end - 1) + i
            cost2 = self.solve(start + 1, end) + i
            cost = max(cost1, cost2)
            ans = min(ans, cost)
        return ans

    def getMoneyAmount(self, n: int) -> int:
        return self.solve(1, n)


if __name__ == "__main__":
    print(Solution().getMoneyAmount(4))
