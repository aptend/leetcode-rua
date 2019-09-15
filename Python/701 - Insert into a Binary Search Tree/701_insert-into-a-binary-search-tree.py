from leeyzer import Solution, solution
from leeyzer.assists import TreeContext, TreeNode


class Q701(Solution):
    @solution
    def insertIntoBST(self, root, val):
        # 96ms 91.77% / 108ms
        if root is None:
            return TreeNode(x=val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root


def main():
    q = Q701()
    q.set_context(TreeContext)
    q.add_args([4, 2, 7, 1, 3], 5)
    q.add_args([4, 2, 7, 1, 3], 3)
    q.run()


if __name__ == "__main__":
    main()
