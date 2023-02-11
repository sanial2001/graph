# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, graph):
        if not node:
            return None
        l, r = self.dfs(node.left, graph), self.dfs(node.right, graph)
        if l:
            graph[node.val].append(l.val)
            graph[l.val].append(node.val)
        if r:
            graph[node.val].append(r.val)
            graph[r.val].append(node.val)
        node.left, node.right = l, r
        return node

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = collections.defaultdict(list)
        self.dfs(root, graph)

        q, visit = [start], set()
        visit.add(start)
        steps = 0
        while q:
            num = len(q)
            for i in range(num):
                node = q.pop(0)
                for nei in graph[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            if q: steps += 1

        return steps
