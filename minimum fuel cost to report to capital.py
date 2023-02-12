class Solution:
    def dfs(self, graph, node, visit, seats):
        total_people, total_fuel = 1, 0
        for nei in graph[node]:
            if nei not in visit:
                visit.add(nei)
                people, car, fuel = self.dfs(graph, nei, visit, seats)
                total_people += people
                total_fuel += fuel
        cars_needed = math.ceil(total_people / seats)
        # print(node, total_people, cars_needed, total_fuel+cars_needed)
        return [total_people, cars_needed, total_fuel + cars_needed]

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(list)
        visit = set()
        visit.add(0)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        people, cars, fuel = self.dfs(graph, 0, visit, seats)
        return fuel - cars
