from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q687(Solution):
    @solution
    def longestUnivaluePath(self, root):
        # 456ms 39%
        self.ans = 0
        self.longest_uni(root)
        return self.ans

    def longest_uni(self, node):
        if node is None:
            return 0
        l = self.longest_uni(node.left)
        r = self.longest_uni(node.right)
        if node.left and node.left.val == node.val:
            l += 1
        else:
            l = 0
        if node.right and node.right.val == node.val:
            r += 1
        else:
            r = 0
        self.ans = max(self.ans, l + r)
        return max(l, r)
        


def main():
    q = Q687()
    q.set_context(TreeContext)
    q.add_args([5, 4, 5, 1, 1, 5])
    q.add_args([4, 4, 4, 4, 4, None, 5])
    q.run()


if __name__ == "__main__":
    main()
