from leezy import solution, Solution


class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.cc = n

    def _find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def connect(self, p, q):
        pp = self._find(p)
        pq = self._find(q)
        if pq == pp:
            return True
        if self.rank[pp] > self.rank[pq]:
            self.parent[pq] = pp
        elif self.rank[pp] < self.rank[pq]:
            self.parent[pp] = pq
        else:
            self.rank[pq] += 1
            self.parent[pp] = pq
        self.cc -= 1
        return False

    def __str__(self):
        return f"{self.cc} connected components. {self.parent}"

class Q1319(Solution):
    @solution
    def makeConnected(self, n, connections):
        uf = UF(n)
        spare_conn = 0
        for p, q in connections:
            if uf.connect(p, q):
                spare_conn += 1
        needed_conn = uf.cc - 1
        return needed_conn if spare_conn >= needed_conn else -1


def main():
    q = Q1319()
    q.add_case(q.case(4, [[0, 1], [0, 2], [1, 2]]).assert_equal(1))
    q.add_case(q.case(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]).assert_equal(2))
    q.add_case(q.case(6, [[0, 1], [0, 2], [0, 3], [1, 2]]).assert_equal(-1))
    q.add_case(q.case(5, [[0, 1], [0, 2], [3, 4], [2, 3]]).assert_equal(0))
    q.run()

if __name__ == '__main__':
    main()
