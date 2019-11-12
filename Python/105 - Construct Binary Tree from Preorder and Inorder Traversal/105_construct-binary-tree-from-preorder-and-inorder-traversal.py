from leezy import solution, Solution
from leezy.assists import TreeNode


class Q105(Solution):
    @solution
    def buildTree(self, preorder, inorder):
        # 192ms 39.55%
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        i = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:i+1], inorder[:i])
        node.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return node

    @solution
    def build_tree(self, preorder, inorder):
        # 96ms 73.61%
        def cons(p1, p2, i1, i2):
            if p1 > p2:
                return None
            node = TreeNode(preorder[p1])
            sep = inorder.index(node.val)
            node.left = cons(p1+1, p1+sep-i1, i1, sep-1)
            node.right = cons(p1+sep-i1+1, p2, sep+1, i2)
            return node
        N = len(preorder)
        return cons(0, N-1, 0, N-1)


def main():
    q = Q105()
    q.add_args([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    q.run()


if __name__ == '__main__':
    main()
