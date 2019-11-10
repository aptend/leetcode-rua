from leezy import Solution, solution
from leezy.assists import TreeContext


class Q450(Solution):
    @solution
    def deleteNode(self, root, key):
        # 48ms 94.41%
        if root is None:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # r_min = self.min(root.right)
            # r_min.right = self.delete_min(root.right)
            # r_min.left = root.left
            r_min = root.right
            while r_min.left:
                r_min = r_min.left
            r_min.right = self.deleteNode(root.right, r_min.val)
            r_min.left = root.left
            root = r_min
        return root

    def min(self, node):
        if node is None:
            return
        while node.left:
            node = node.left
        return node

    def delete_min(self, node):
        if node is None:
            return
        if not node.left:
            return node.right
        node.left = self.delete_min(node.left)
        return node


def main():
    q = Q450()
    q.set_context(TreeContext)
    q.add_args([5, 3, 6, 2, 4, None, 7], 42)
    q.add_args([5, 3, 6, 2, 4, None, 7], 3)
    q.add_args([5, 3, 6, 2, 4, None, 7], 5)
    q.run()


if __name__ == "__main__":
    main()
