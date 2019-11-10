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
            self.parents[rp] = rq
            self.ranks[rq] += 1
        self.count -= 1


class Q990(Solution):
    @solution
    def equationsPossible(self, equations):
        # 32ms 71.73%
        base = ord('a')
        uf = UF(26)
        for eq in equations:
            if eq[1] == '=':
                uf.union(ord(eq[0])-base, ord(eq[3])-base)
        for eq in equations:
            if eq[1] == '!':
                if uf.connected(ord(eq[0])-base, ord(eq[3])-base):
                    return False
        return True


def main():
    q = Q990()
    q.add_args(['a==b', 'b!=a'])  # f
    q.add_args(['a==b', 'b==a'])  # t
    q.add_args(["a==b", "b==c", "a==c"])  # t
    q.add_args(["a==b", "b!=c", "c==a"])  # f
    q.add_args(["c==c", "b==d", "x!=z"])  # t
    q.run()


if __name__ == "__main__":
    main()
