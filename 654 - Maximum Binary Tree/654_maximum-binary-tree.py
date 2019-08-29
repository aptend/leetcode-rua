from leeyzer import Solution, solution
from leeyzer.assists import TreeNode


class Q654(Solution):
    @solution
    def constructMaximumBinaryTree(self, nums):
        # 168ms 81.83%
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        sep = nums.index(max(nums))
        node = TreeNode(nums[sep])
        node.left = self.constructMaximumBinaryTree(nums[:sep])
        node.right = self.constructMaximumBinaryTree(nums[sep+1:])
        return node

    @solution
    def construct_iter(self, nums):
        # 152ms 94.09%
        stack = []
        for x in nums:
            node = None
            while stack and stack[-1].val < x:
                tmp = stack.pop()
                tmp.right = node
                node = tmp
            cur_node = TreeNode(x)
            cur_node.left = node
            stack.append(cur_node)
        root = None
        while stack:
            node = stack.pop()
            node.right = root
            root = node
        return root



def main():
    q = Q654()
    q.add_args([3, 2, 1, 6, 0, 5])
    q.run()


if __name__ == "__main__":
    main()
