from leezy import Solution, solution


class UF:
    def __init__(self, size=0):
        self.parents = list(range(size))
        self.ranks = [0] * size
        self.count = size

    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

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
            self.parents[rq] = rp
            self.ranks[rp] += 1
        self.count -= 1


class Q684(Solution):
    @solution
    def findRedundantConnection(self, edges):
        # 36ms 93.23%
        uf = UF(len(edges)+1)
        # since there's only one redundant edge
        # we can iter orderly
        for edge in edges:
            p, q = edge[0], edge[1]
            if uf.connected(p, q):
                return edge
            else:
                uf.union(p, q)


def main():
    q = Q684()
    q.add_args([[1, 2], [1, 3], [2, 3]])
    q.add_args([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    q.run()


if __name__ == "__main__":
    main()
