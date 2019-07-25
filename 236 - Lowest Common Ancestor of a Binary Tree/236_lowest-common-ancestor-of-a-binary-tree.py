from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q236(Solution):
    @solution
    def lowestCommonAncestor(self, root, p, q):
        # 68ms 64.81%
        if root is None:
            return
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if root.val == p or root.val == q:
            return root
        if l and r:
            return root
        else:
            return l or r


def main():
    q = Q236()
    q.set_context(TreeContext)
    t1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    q.add_args(t1, 5, 1)
    q.add_args(t1, 5, 2)
    q.add_args(t1, 2, 0)
    q.run()


if __name__ == "__main__":
    main()
