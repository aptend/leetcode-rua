from leezy import Solution, solution
from leezy.assists import TreeContext

class Q1038(Solution):
    @solution
    def bst_to_gst(self, root):
        # 16ms 80.30%
        def modify(node, base):
            if node is None:
                return None, base
            rnode, rval = modify(node.right, base)
            node.val += rval
            node.right = rnode
            lnode, lval = modify(node.left, node.val)
            node.left = lnode
            return node, lval
        m_root, _ = modify(root, 0)
        return m_root

    @solution
    def bstToGst(self, root):
        # 16ms 80.30%
        # maintaining a global variable makes things more simple and straight
        self.base = 0
        def modify(node):
            if node is None:
                return
            modify(node.right)
            self.base += node.val
            node.val = self.base
            modify(node.left)
        modify(root)
        return root

    

def main():
    q = Q1038()
    q.set_context(TreeContext)
    q.add_args([])
    q.add_args([1, None, 2])
    q.add_args([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    q.run()


if __name__ == "__main__":
    main()
