from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q230(Solution):
    @solution
    def kthSmallest(self, root, k):
        # 36ms 93.60%
        self.order = 0
        def inorder(node):
            if node is None:
                return
            ans = inorder(node.left)
            if ans is not None:
                return ans
            self.order += 1
            if self.order == k:
                return node.val
            return inorder(node.right)
        return inorder(root)


def main():
    q = Q230()
    q.set_context(TreeContext)
    q.add_args([3, 1, 4, None, 2], 1)
    q.add_args([5, 3, 6, 2, 4, None, None, 1], 3)
    q.run()


if __name__ == "__main__":
    main()
