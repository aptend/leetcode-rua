from leezy import Solution, solution
from leezy.assists import TreeContext


class Q101(Solution):
    @solution
    def isSymmetric(self, root):
        # 20ms
        if root is None:
            return True
        return self.scan(root.left, root.right)

    def scan(self, p, q):
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.scan(p.left, q.right) and self.scan(p.right, q.left)
        else:
            return False

    @solution
    def is_sysmetric_iter(self, root):
        # 16ms 95.09%
        if root is None:
            return True
        stack_left = [root.left]
        stack_right = [root.right]
        while stack_left and stack_right:
            left = stack_left.pop()
            right = stack_right.pop()
            if left is None and right is None:
                continue
            if left and right and left.val == right.val:
                stack_left.append(left.right)
                stack_left.append(left.left)
                stack_right.append(right.left)
                stack_right.append(right.right)
            else:
                return False
        return len(stack_left) == len(stack_right)


def main():
    q = Q101()
    q.set_context(TreeContext)
    q.add_args([1, 2, 2, 3, 4, 4, 3])
    q.add_args([1, 2, 2, None, 3, None, 3])
    q.add_args([2, 3, 3, 4, 5, None, 4])
    q.run()


if __name__ == "__main__":
    main()
