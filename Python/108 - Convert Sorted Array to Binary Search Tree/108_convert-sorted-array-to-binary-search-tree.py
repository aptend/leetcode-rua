from leezy import Solution, solution
from leezy.assists import TreeNode

class Q108(Solution):
    @solution
    def sortedArrayToBST(self, nums):
        # 48ms 96.35%
        def construct(lo, hi):
            if lo > hi:
                return None
            mid = lo + (hi - lo) // 2
            node = TreeNode(nums[mid])
            node.left = construct(lo, mid-1)
            node.right = construct(mid+1, hi)
            return node
        return construct(0, len(nums)-1)

def main():
    q = Q108()
    q.add_args([-10, -3, 0, 5, 9])
    q.add_args(list(range(10)))
    q.run()


if __name__ == "__main__":
    main()
