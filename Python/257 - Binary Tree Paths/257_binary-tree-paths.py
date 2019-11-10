from leezy import Solution, solution
from leezy.assists import TreeContext


class Q257(Solution):
    @solution
    def binaryTreePaths(self, root):
        # 20ms 71.19%
        if root is None:
            return ""
        current, total = [], []
        self.collect(root, current, total)
        return total

    def collect(self, node, current, total):
        if not node.left and not node.right:
            current.append(str(node.val))
            total.append("->".join(current))
            current.pop()
            return
        current.append(str(node.val))
        if node.left:
            self.collect(node.left, current, total)
        if node.right:
            self.collect(node.right, current, total)
        current.pop()


def main():
    q = Q257()
    q.set_context(TreeContext)
    q.add_args([1, 2, 3, None, 5])
    q.add_args([])
    q.add_args([42])
    q.add_args([1, 2, 3])
    q.add_args([4, 9, 0, 5, 1])
    q.run()


if __name__ == "__main__":
    main()
