import math


def solve(n, nums, q, queries):
    ans = []
    for q in queries:
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = math.gcd(nums[i], nums[j])
                if x % q == 0:
                    res += 1
        ans.append(res)
    return ans


if __name__ == "__main__":
    print(solve(3, [4, 8, 9], 2, [2, 5]))
