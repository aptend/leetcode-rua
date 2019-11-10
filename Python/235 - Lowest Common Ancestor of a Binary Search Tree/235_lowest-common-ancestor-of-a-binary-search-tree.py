from leezy import Solution, solution
from leezy.assists import TreeContext


class Q235(Solution):
    @solution
    def lowestCommonAncestor(self, root, p, q):
        # 68ms
        if p < root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)
        if p > root.val < q:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    @solution
    def lca_iter(self, root, p, q):
        # 76ms 40.62%
        while root:
            if root.val > p and root.val > q:
                root = root.left
            elif root.val < p and root.val < q:
                root = root.right
            else:
                return root

    def lca_dumb(self, root, p, q):
        ppath, qpath = [], []
        self.search(root, p, ppath)
        self.search(root, q, qpath)
        prev = x = y = None
        for x, y in zip(ppath, qpath):
            if x.val != y.val:
                return prev
            prev = x
        return x

    def search(self, node, v, path):
        if node is None:
            path.clear()
            return
        if v == node.val:
            path.append(node)
            return
        path.append(node)
        if v > node.val:
            self.search(node.right, v, path)
        else:
            self.search(node.left, v, path)


def main():
    q = Q235()
    q.set_context(TreeContext)
    t1 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    q.add_args(t1, 2, 8)
    q.add_args(t1, 2, 4)
    q.add_args(t1, 3, 7)
    q.run()


if __name__ == "__main__":
    main()
