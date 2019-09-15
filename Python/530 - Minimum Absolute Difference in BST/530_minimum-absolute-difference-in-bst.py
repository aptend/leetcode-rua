from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q530(Solution):
    @solution
    def getMinimumDifference(self, root):
        # 36ms 99.60%
        self.ans = float('inf')
        self.prev = None
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.ans

    @solution
    def minimum_diff(self, root):
        # 40ms
        # at least two nodes, no need to check if root is None 
        self.ans = float('inf')
        def min_diff(node):
            if node.left is None and node.right is None:
                return node.val, node.val
            min_ = max_ = node.val
            if node.left:
                l_min, l_max = min_diff(node.left)
                self.ans = min(self.ans, node.val-l_max)
                min_ = l_min
            if node.right:
                r_min, r_max = min_diff(node.right)
                self.ans = min(self.ans, r_min - node.val)
                max_ = r_max
            return min_, max_
        min_diff(root)
        return self.ans


def main():
    q = Q530()
    q.set_context(TreeContext)
    q.add_args([1, None, 3, 2])
    q.add_args([1, None, 15, 3, 80])
    q.run()


if __name__ == "__main__":
    main()
