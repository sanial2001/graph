import heapq

class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        nums = sorted(zip(efficiency, speed), reverse=True)
        ans, pq, sums = 0, [], 0
        for e, s in nums:
            heapq.heappush(pq, s)
            sums += s
            if len(pq) > k:
                sums -= heapq.heappop(pq)
            ans = max(ans, sums*e)
        return ans % (10**9 + 7)