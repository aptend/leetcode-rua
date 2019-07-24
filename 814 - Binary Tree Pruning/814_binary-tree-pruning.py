from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q814(Solution):
    @solution
    def pruneTree(self, root):
        # 16ms 88.68%
        if root is None:
            return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if root.val == 0 and not left and not right:
            return None
        root.left = left
        root.right = right
        return root


def main():
    q = Q814()
    q.set_context(TreeContext)
    q.add_args([1, None, 0, 0, 1])
    q.add_args([1, 0, 1, 0, 0, 0, 1])
    q.add_args([1, 1, 0, 1, 1, 0, 1, 0])
    q.run()


if __name__ == "__main__":
    main()
