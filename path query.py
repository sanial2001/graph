import collections

if __name__ == "__main__":
    g = collections.defaultdict(list)
    g[1].append([2, 4])

    for u, v in g[1]:
        print(u, v)