from leezy import Solution, solution
from leezy.assists import TreeContext

class Q104(Solution):
    @solution
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def main():
    q = Q104()
    q.set_context(TreeContext)
    q.add_args([3, 9, 20, None, None, 15, 7])
    q.run()


if __name__ == "__main__":
    main()
