from leezy import solution, Solution
from leezy.assists import TreeContext


class Q1026(Solution):
    @solution
    def maxAncestorDiff(self, root):
        self.ans = 0

        def walk(node):
            if node is None:
                return None, None
            l = walk(node.left)
            r = walk(node.right)
            v = node.val
            if l[0] is None:
                l = (v, v)
            if r[0] is None:
                r = (v, v)
            min_, max_ = min(l[0], r[0]), max(l[1], r[1])
            self.ans = max(self.ans, max(abs(v-min_), abs(v-max_)))
            return (min(v, min_), max(v, max_))
        walk(root)
        return self.ans


def main():
    q = Q1026()
    q.set_context(TreeContext)
    q.add_case(q.case([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]))
    q.add_case(q.case([0, None, 1]))
    q.run()


if __name__ == '__main__':
    main()
