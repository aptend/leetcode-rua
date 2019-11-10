from leezy import solution, Solution
from leezy.assists import TreeContext

class Q617(Solution):
    @solution
    def mergeTrees(self, t1, t2):
        # 72ms 99%
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


def main():
    q = Q617()
    q.set_context(TreeContext)
    q.add_args([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7])
    q.run()

if __name__ == '__main__':
    main()
