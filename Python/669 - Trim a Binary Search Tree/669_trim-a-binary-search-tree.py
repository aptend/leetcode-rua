from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q669(Solution):
    @solution
    def trimBST(self, root, L, R):
        # 44ms 57.38%
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


def main():
    q = Q669()
    q.set_context(TreeContext)
    q.add_args([1, 0, 2], 1, 2)
    q.add_args([3, 0, 4, None, 2, None, None, 1], 1, 3)
    q.run()


if __name__ == "__main__":
    main()
