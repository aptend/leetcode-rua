from leezy import Solution, solution


class UF:
    def __init__(self, size):
        self.parents = list(range(size))
        self.ranks = [0] * size
        self.count = size

    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return
        if self.ranks[rp] > self.ranks[rq]:
            self.parents[rq] = rp
        elif self.ranks[rp] < self.ranks[rq]:
            self.parents[rp] = rq
        else:
            self.parents[rp] = rq
            self.ranks[rq] += 1
        self.count -= 1


class Q839(Solution):
    @solution
    def numSimilarGroups(self, A):
        # 3848ms 84.35%
        def is_similar(s, t):
            diff = 0
            for x, y in zip(s, t):
                if x != y:
                    diff += 1
                if diff > 2:
                    return False
            return diff == 2

        n, m = len(A), len(A[0])
        uf = UF(n)
        if n <= m:
            # m * n * n
            for i in range(n):
                for j in range(i+1, n):
                    if is_similar(A[i], A[j]):
                        uf.union(i, j)
        else:
            # n * m * m
            setA = {a: idx for idx, a in enumerate(A)}
            for idx, a in enumerate(A):
                for i in range(m-1):
                    for j in range(i+1, m):
                        r_a = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                        if r_a in setA:
                            uf.union(idx, setA[r_a])
        return uf.count


def main():
    q = Q839()
    q.add_args(['tars', 'rats', 'arts', 'star'])
    q.run()


if __name__ == "__main__":
    main()
