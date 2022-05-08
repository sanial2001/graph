import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pq = []
        for j in range(n):
            heapq.heappush(pq, (nums1[0] + nums2[j], 0, j))
        ans = []
        while pq and k > 0:
            sums, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if i+1 < m:
                heapq.heappush(pq, (nums1[i+1]+nums2[j], i+1, j))
            k = k-1
        return ans