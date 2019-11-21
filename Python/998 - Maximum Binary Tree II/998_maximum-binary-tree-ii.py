from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode


class Q998(Solution):
    @solution
    def insertIntoMaxTree(self, root, val):
        # 24ms 98.86%
        if root is None:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root


def main():
    q = Q998()
    q.set_context(TreeContext)
    q.add_case(q.case([4, 1, 3, None, None, 2], 5))
    q.add_case(q.case([5, 2, 4, None, 1], 3))
    q.add_case(q.case([5, 2, 3, None, 1], 4))
    q.run()

if __name__ == '__main__':
    main()
