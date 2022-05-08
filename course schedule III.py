class Solution:
    def scheduleCourse(self, courses) -> int:
        courses.sort(key=lambda x: x[1])
        pq, sums = [], 0
        for dur, last in courses:
            pq.append(dur)
            sums += dur
            if sums > last:
                sums -= max(pq)
                pq.remove(max(pq))
        return len(pq)
