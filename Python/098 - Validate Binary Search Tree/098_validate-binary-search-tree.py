from leezy import Solution, solution
from leezy.assists import TreeContext


class Q098(Solution):
    @solution
    def isValidBST(self, root):
        # 28ms 95.04%
        if root is None:
            return True
        def valid(node):
            if not node.left and not node.right:
                return True, node.val, node.val
            min_ = max_ = node.val
            if node.left:
                ok, l_min, l_max = valid(node.left)
                if not ok or node.val <= l_max:
                    return False, -1, -1
                min_ = l_min
            if node.right:
                ok, r_min, r_max = valid(node.right)
                if not ok or node.val >= r_min:
                    return False, -1, -1
                max_ = r_max
            return True, min_, max_
        return valid(root)[0]


    @solution
    def is_valid(self, root):
        # 32ms
        def check(node, lo, hi):
            if node is None:
                return True
            if node.val >= hi or node.val <= lo:
                return False
            return check(node.left, lo, node.val) and check(node.right, node.val, hi)
        return check(root, float('-inf'), float('inf'))
    
    @solution
    def is_valid_inorder(self, root):
        # 28ms
        self.prev = None
        def inoder(node):
            if node is None:
                return True
            if not inoder(node.left):
                return False
            if self.prev is not None and self.prev >= node.val:
                return False
            self.prev = node.val
            return inoder(node.right)
        return inoder(root)


def main():
    q = Q098()
    q.set_context(TreeContext)
    q.add_args([0, None, -1])
    q.add_args([2, 1, 3])
    q.add_args([5, 1, 4, None, None, 3, 6])
    q.run()


if __name__ == "__main__":
    main()
