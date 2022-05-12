class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        visit = set()
        visit.add(0)
        q = [0]
        while q:
            curr = q.pop(0)
            if curr == targetCapacity:
                return True
            for step in [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]:
                new = curr + step
                if 0 < new <= jug1Capacity + jug2Capacity and new not in visit:
                    visit.add(new)
                    q.append(new)
        return False
