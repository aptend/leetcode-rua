from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q094(Solution):
    @solution
    def inorderTraversal(self, root):
        # 16ms
        vals = []
        self.trav(root, vals)
        return vals

    def trav(self, node, vals):
        if node is None:
            return
        self.trav(node.left, vals)
        vals.append(node.val)
        self.trav(node.right, vals)
    
    @solution
    def inorder_iter(self, root):
        # 12ms 94.31%
        vals, stack = [], []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                break
            n = stack.pop()
            vals.append(n.val)
            node = n.right
        return vals

def main():
    q = Q094()
    q.set_context(TreeContext)
    q.add_args([1, None, 2, 3])
    q.add_args([None])
    q.run()


if __name__ == "__main__":
    main()
