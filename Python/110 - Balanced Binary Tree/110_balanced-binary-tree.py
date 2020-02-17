from leezy import Solution, solution
from leezy.assists import TreeContext

class Q110(Solution):
    @solution
    def isBalanced(self, root):
        # 40ms 80%
        p, _ = self.walk(root)
        return p

    def walk(self, node):
        if node is None:
            return True, 0
        lp, lh = self.walk(node.left)
        if not lp:
            return False, -1
        rp, rh = self.walk(node.right)
        if not rp:
            return False, -1
        if abs(lh - rh) > 1:
            return False, -1
        return True, max(lh, rh)+1

    @solution
    def is_balanced(self, root):
        def check(node):
            if node is None:
                return 0
            left_h = check(node.left)
            right_h = check(node.right)
            if left_h < 0 or right_h < 0 or abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1
        return check(root) >= 0


def main():
    q = Q110()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]).assert_equal(True))
    q.add_case(q.case([1, 2, 2, 3, 3, None, None, 4, 4]).assert_equal(False))
    q.run()


if __name__ == "__main__":
    main()
