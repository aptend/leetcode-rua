from leezy import Solution, solution
from leezy.assists import TreeContext


class Q129(Solution):
    @solution
    def sumNumbers(self, root):
        # 20ms 71.23%
        if root is None:
            return 0
        self.ans = 0
        self.collect(root, 0)
        return self.ans

    def collect(self, node, val):
        if not node.left and not node.right:
            self.ans += val * 10 + node.val
            return
        val = val * 10 + node.val
        if node.left:
            self.collect(node.left, val)
        if node.right:
            self.collect(node.right, val)


def main():
    q = Q129()
    q.set_context(TreeContext)
    q.add_args([])
    q.add_args([42])
    q.add_args([1, 2, 3])
    q.add_args([4, 9, 0, 5, 1])
    q.run()


if __name__ == "__main__":
    main()
