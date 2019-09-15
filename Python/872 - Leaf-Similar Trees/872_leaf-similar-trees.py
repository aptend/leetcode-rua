from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q872(Solution):
    @solution
    def leafSimilar(self, root1, root2):
        # 8ms 99.65%
        leafs1, leafs2 = [], []
        self.dfs(root1, leafs1)
        self.dfs(root2, leafs2)
        return leafs1 == leafs2

    def dfs(self, node, leafs):
        if node is None:
            return 
        if not node.left and not node.right:
            leafs.append(node.val)
        if node.left:
            self.dfs(node.left, leafs)
        if node.right:
            self.dfs(node.right, leafs)


def main():
    q = Q872()
    q.set_context(TreeContext)
    q.add_args([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], 
               [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    q.run()


if __name__ == "__main__":
    main()
