from collections import defaultdict

from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q508(Solution):
    @solution
    def findFrequentTreeSum(self, root):
        # 32ms 97.37%
        if root is None:
            return []
        counter = defaultdict(int)
        def subsum(node):
            if node is None:
                return 0
            s = node.val + subsum(node.left) + subsum(node.right)
            counter[s] += 1
            return s
        subsum(root)
        most_common = max(counter.values())
        return [k for k, v in counter.items() if v == most_common]


def main():
    q = Q508()
    q.set_context(TreeContext)
    q.add_args([5, 2, -3])
    q.add_args([5, 2, -5])
    q.run()


if __name__ == "__main__":
    main()
