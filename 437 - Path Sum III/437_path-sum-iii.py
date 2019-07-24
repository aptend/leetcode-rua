from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q437(Solution):
    @solution
    def pathSum(self, root, sum):
        # 1088ms 18.56%
        if root is None:
            return 0
        return (self.path_from_here(root, sum) +
                self.pathSum(root.left, sum) +
                self.pathSum(root.right, sum))

    def path_from_here(self, node, target):
        if node is None:
            return 0
        target -= node.val
        here_count = int(target == 0)
        return (here_count +
                self.path_from_here(node.left, target) +
                self.path_from_here(node.right, target))


def main():
    q = Q437()
    q.set_context(TreeContext)
    q.add_args([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8)
    q.run()


if __name__ == "__main__":
    main()
