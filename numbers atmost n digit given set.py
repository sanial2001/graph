from collections import deque
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        res = 0
        q, visit = deque(), set()
        for num in digits:
            if int(num) <= n:
                res += 1
                q.append(num)
                visit.add(num)

        while q:
            num = len(q)
            for i in range(num):
                val = q.popleft()
                for j in range(len(digits)):
                    new_val = val + digits[j]
                    if int(new_val) <= n and new_val not in visit:
                        res += 1
                        q.append(new_val)
                        visit.add(new_val)

        return res
