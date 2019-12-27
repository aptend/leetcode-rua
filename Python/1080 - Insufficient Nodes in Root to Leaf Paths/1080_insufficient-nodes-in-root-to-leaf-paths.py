from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode


class Q1080(Solution):
    @solution
    def sufficientSubset(self, root, limit):
        # 88ms 84.01%
        if not root:
            return None
        if not (root.left or root.right):
            if limit - root.val > 0:
                return None
            else:
                return root
        root.left = self.sufficientSubset(root.left, limit-root.val)
        root.right = self.sufficientSubset(root.right, limit-root.val)
        if not (root.left or root.right):
            return None
        else:
            return root


def main():
    q = Q1080()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14], 1)
                .assert_equal(TreeNode.make_tree([1, 2, 3, 4, None, None, 7, 8, 9, None, 14])))

    q.add_case(q.case([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3], 22)
               .assert_equal(TreeNode.make_tree([5, 4, 8, 11, None, 17, 4, 7, None, None, None, 5])))

    q.add_case(q.case([5, -6, -6], 0).assert_equal(None))
    q.run()

if __name__ == '__main__':
    main()
