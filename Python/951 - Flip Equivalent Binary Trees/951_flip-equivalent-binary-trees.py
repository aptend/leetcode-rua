from leezy import Solution, solution
from leezy.assists import TreeContext


class Q951(Solution):
    @solution
    def flipEquiv(self, root1, root2):
        # 16ms 86.76ms
        # but how about time complexity?
        # https://www.wikiwand.com/en/Master_theorem_(analysis_of_algorithms)
        # we can say that a subproblem costs T(n) only when root1.val == root2.val
        # because each value in tree is unique,
        # there are at most 2 T(n/2) subproblem among the 4 subproblem
        # the recurrence relation can be expressed by
        # T(n) = 2T(n/2) + O(1) -> O(n) -> O(min(N1, N2))
        # on the other hand, if each value is not unique:
        # T(n) = 4T(n/2) + O(1) -> O(min(N1, N2)^2)

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
