from leezy import Solution, solution
from leezy.assists import TreeNode


class Q106(Solution):
    @solution
    def buildTree(self, inorder, postorder):
        # 104ms 71.43%
        N = len(inorder)
        def construct(i, j, p, q):
            if i > j:
                return None
            if i == j:
                return TreeNode(inorder[i])
            x = postorder[q]
            node = TreeNode(x)
            k = inorder.index(x)
            left_n = k - i
            node.left = construct(i, k-1, p, p+left_n-1)
            node.right = construct(k+1, j, p+left_n, q-1)
            return node
        return construct(0, N-1, 0, N-1)


def main():
    q = Q106()
    q.add_args([1, 2, 3], [3, 2, 1])
    q.add_args([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    q.run()


if __name__ == "__main__":
    main()
