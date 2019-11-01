from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q124(Solution):
    @solution
    def maxPathSum(self, root):
        # 72ms 96.53%
        self.ans = float('-inf')
        self.max_sum_at(root)
        return self.ans

    def max_sum_at(self, node):
        if node is None:
            return 0
        l = self.max_sum_at(node.left) + node.val
        r = self.max_sum_at(node.right) + node.val
        self.ans = max(self.ans, l + r - node.val)
        return max(l, r, 0)


def main():
    q = Q124()
    q.set_context(TreeContext)
    q.add_args([1, 2, 3]) # 6
    q.add_args([-10, 9, 20, None, None, 15, 7]) # 42
    q.add_args([-3]) # -3
    q.add_args([2, -1]) # 2
    q.run()


if __name__ == "__main__":
    main()
