from leezy import Solution, solution
from leezy.assists import TreeContext

class Q783(Solution):
    @solution
    def minDiffInBST(self, root):
        # 12ms 96.70%
        nums = []
        ans = float('inf')

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        for i, j in zip(nums, nums[1:]):
            ans = min(ans, j-i)
        return ans
    
    @solution
    def min_diff_bst(self, root):
        # 16ms
        self.pre_val = float('-inf')
        self.ans = float('inf')
        def min_diff(node):
            if node is None:
                return
            min_diff(node.left)
            self.ans = min(self.ans, node.val - self.pre_val)
            self.pre_val = node.val
            min_diff(node.right)
        min_diff(root)
        return self.ans



def main():
    q = Q783()
    q.set_context(TreeContext)
    q.add_args([4, 2, 6, 1, 3, None, None])
    q.run()


if __name__ == "__main__":
    main()
