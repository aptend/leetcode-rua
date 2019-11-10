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


def main():
    q = Q110()
    q.set_context(TreeContext)
    q.add_args([3, 9, 20, None, None, 15, 7])
    q.add_args([1, 2, 2, 3, 3, None, None, 4, 4])
    q.run()


if __name__ == "__main__":
    main()
