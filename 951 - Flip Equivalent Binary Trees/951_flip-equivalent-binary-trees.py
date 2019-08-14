from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q951(Solution):
    @solution
    def flipEquiv(self, root1, root2):
        # 16ms 86.76ms
        # but how about time complexity?
        if not root1 and not root2:
            return True
        if root1 is None or root2 is None or root1.val != root2.val:
            return False
        if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
            return True
        else:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)


def main():
    q = Q951()
    q.set_context(TreeContext)
    q.add_args([1, 2, 3, 4, 5, 6, None, None, None, 7, 8],
               [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])
    q.add_args([1], [1,2])
    q.run()


if __name__ == "__main__":
    main()
