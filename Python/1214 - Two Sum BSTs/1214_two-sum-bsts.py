from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

from bisect import bisect_left

class Q1214(Solution):
    @solution
    def twoSumBSTs(self, root1, root2, target):
        def flat(node, cur):
            if node is None:
                return
            flat(node.left, cur)
            cur.append(node.val)
            flat(node.right, cur)
        t1 = []
        flat(root1, t1)
        t2 = []
        flat(root2, t2)
        for x in t1:
            idx = bisect_left(t2, target - x)
            if idx < len(t2) and t2[idx] == target - x:
                return True
        return False


def main():
    q = Q1214()
    q.set_context(TreeContext)
    q.add_args([2, 1, 4], [1, 0, 3], 5)
    q.run()


if __name__ == "__main__":
    main()
