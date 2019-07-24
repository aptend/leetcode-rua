from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q112(Solution):
    @solution
    def hasPathSum(self, root, sum):
        # 28ms 92.74%
        # 44ms 11.73%
        # 64ms 5.75%
        if root is None:
            return sum == 0
        if not root.left and not root.right:
            return sum == root.val
        if root.left and self.hasPathSum(root.left, sum-root.val):
            return True
        if root.right and self.hasPathSum(root.right, sum-root.val):
            return True
        return False


def main():
    q = Q112()
    q.set_context(TreeContext)
    q.add_args([5], 9)
    q.add_args([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 9)
    q.add_args([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22)
    q.run()


if __name__ == "__main__":
    main()
