from leezy import solution, Solution
from leezy.assists import TreeContext

class Q993(Solution):
    @solution
    def isCousins(self, root, x, y):
        # 32ms 91.32%
        def find(node, prev, v, lv):
            if not node:
                return None, None
            if node.val == v:
                return prev, lv
            p, l = find(node.left, node, v, lv + 1)
            if p:
                return p, l
            p, l = find(node.right, node, v, lv + 1)
            return p, l
        xp, xl = find(root, root, x, 0)
        if not xp:
            return False
        yp, yl = find(root, root, y, 0)
        return xl == yl and xp is not yp


def main():
    q = Q993()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, 4], 4, 3).assert_equal(False))
    q.add_case(q.case([1, 2, 3, None, 4, None, 5], 4, 5).assert_equal(True))
    q.run()

if __name__ == '__main__':
    main()
