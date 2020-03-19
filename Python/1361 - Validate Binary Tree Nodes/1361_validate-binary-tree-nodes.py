from leezy import solution, Solution


class Q1361(Solution):
    @solution
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        # 364 ms faster than 17.00%
        class UF:
            def __init__(self, n):
                self.parents = list(range(n))
                self.heights = [1] * n
                self.cc = n

            def _find(self, p):
                assert 0 <= p < len(self.parents)
                while p != self.parents[p]:
                    p = self.parents[p]
                return p

            def connect(self, p, q):
                fp = self._find(p)
                fq = self._find(q)
                if fp == fq:
                    return False
                if self.heights[fp] < self.heights[fq]:
                    self.parents[fp] = fq
                elif self.heights[fq] < self.heights[fp]:
                    self.parents[fq] = fp
                else:
                    self.parents[fp] = fq
                    self.heights[fq] += 1
                self.cc -= 1
                return True

        uf = UF(n)
        for i, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l >= 0:
                if not uf.connect(i, l):
                    return False
            if r >= 0:
                if not uf.connect(i, r):
                    return False
        return uf.cc == 1

    @solution
    def validate_bt(self, n, leftChild, rightChild):
        # 328 ms faster than 32.71%
        # every non-root node in a tree, in_degree = 1, out_degree = [0, 1, 2]
        # and there is only one root node
        stat = [[0, 0] for _ in range(n)]
        for i, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l >= 0:
                stat[i][1] += 1
                stat[l][0] += 1
            if r >= 0:
                stat[i][1] += 1
                stat[r][0] += 1
        root_found = False
        for ind, outd in stat:
            if ind == 0:
                if root_found or (n > 1 and outd == 0):
                    return False
                root_found = True
            if ind > 1 or outd > 2:
                return False
        return root_found


def main():
    q = Q1361()
    q.add_case(q.case(4, [1, -1, 3, -1], [2, -1, -1, -1]).assert_equal(True))
    q.add_case(q.case(4, [1, -1, 3, -1], [2, 3, -1, -1]).assert_equal(False))
    q.add_case(q.case(2, [1, 0], [-1, -1]).assert_equal(False))
    q.add_case(q.case(6,
                      [1, -1, -1, 4, -1, -1],
                      [2, -1, -1, 5, -1, -1]).assert_equal(False))
    q.add_case(q.case(4, [1, 2, 0, -1], [-1, -1, -1, -1]).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
