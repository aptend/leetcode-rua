from leezy import Solution, solution
from leezy.assists import TreeContext

class Q543(Solution):
    @solution
    def diameterOfBinaryTree(self, root):
        # 28ms 93.31%
        self.ans = 0
        self.longest(root)
        return self.ans
    def longest(self, node):
        if node is None:
            return -1
        l = self.longest(node.left) + 1
        r = self.longest(node.right) + 1
        self.ans = max(self.ans, l+r)
        return max(l, r)


def main():
    q = Q543()
    q.set_context(TreeContext)
    q.add_args([1, 2, 3, 4, 5])
    q.add_args([1, 2, 3, 4, 5, None, None, 1, 2, 3, 4])
    q.run()


if __name__ == "__main__":
    main()
