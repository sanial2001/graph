class Solution:
    def canCross(self, stones: List[int]) -> bool:
        q = deque()
        q.append((stones[0], 0))
        target = stones[-1]
        visit = set()
        visit.add((stones[0], 0))
        stones = set(stones)

        while q:
            num = len(q)
            for i in range(num):
                stone, step = q.popleft()
                # print(stone, step)
                if stone == target:
                    return True
                move1 = stone + step + 1
                if move1 in stones and (move1, step + 1) not in visit:
                    visit.add((move1, step + 1))
                    q.append((move1, step + 1))
                move2 = stone + step
                if move2 in stones and (move2, step) not in visit:
                    visit.add((move2, step))
                    q.append((move2, step))
                move3 = stone + step - 1
                if move3 in stones and (move3, step - 1) not in visit:
                    visit.add((move3, step - 1))
                    q.append((move3, step - 1))

        return False


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        q = deque()
        q.append((stones[0], 0))
        target = stones[-1]
        visit = set()
        visit.add((stones[0], 0))
        stones = set(stones)

        while q:
            num = len(q)
            for i in range(num):
                stone, step = q.popleft()
                # print(stone, step)
                if stone == target:
                    return True
                for move in [step - 1, step, step + 1]:
                    if (stone + move) in stones and (stone + move, move) not in visit:
                        visit.add((stone + move, move))
                        q.append((stone + move, move))

        return False
