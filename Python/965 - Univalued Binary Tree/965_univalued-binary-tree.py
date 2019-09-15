from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q965(Solution):
    @solution
    def isUnivalTree(self, root):
        # 20ms 65.29%
        val = root.val

        def uni(node):
            if node is None:
                return True
            if node.val != val:
                return False
            return uni(node.left) and uni(node.right)
        return uni(root.left) and uni(root.right)


def main():
    q = Q965()
    q.set_context(TreeContext)
    q.add_args([1, 1, 1, 1, 1, None, 1])
    q.add_args([2, 2, 2, 5, 2])
    q.run()


if __name__ == "__main__":
    main()
