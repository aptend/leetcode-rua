from leezy import solution, Solution
from leezy.assists import TreeContext

class Q1022(Solution):
    @solution
    def sumRootToLeaf(self, root):
        if root is None:
            return 0
        self.ans = 0
        kmod = 10 ** 9 + 7

        def walk(node, v):
            if not (node.left or node.right):
                self.ans = (self.ans + v*2 + node.val) % kmod
            if node.left:
                walk(node.left, v*2 + node.val)
            if node.right:
                walk(node.right, v*2 + node.val)

        walk(root, 0)
        return self.ans


def main():
    q = Q1022()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 0, 1, 0, 1, 0, 1]).assert_equal(22))
    q.run()

if __name__ == '__main__':
    main()
