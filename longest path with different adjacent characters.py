class Solution:
    def dfs(self, tree, tree_char, node):
        if node not in tree:
            return 1
        temp = []
        for child in tree[node]:
            temp.append([tree_char[child], self.dfs(tree, tree_char, child)])
        temp.sort(key=lambda x: x[1])
        cnt, mx = 0, []
        while temp and cnt < 2:
            ch, val = temp.pop()
            if ch != tree_char[node]:
                cnt += 1
                mx.append(val)
        # print(mx)
        self.ans = max(self.ans, sum(mx) + 1)
        return mx[0] + 1 if mx else 0

    def longestPath(self, parent: List[int], s: str) -> int:
        tree = collections.defaultdict(list)
        tree_char = collections.defaultdict(chr)
        n = len(s)
        if n == 1:
            return 1

        for i in range(n):
            tree_char[i] = s[i]

        for i in range(1, n):
            tree[parent[i]].append(i)

        self.ans = 0
        self.dfs(tree, tree_char, 0)
        return self.ans
