from leezy import Solution, solution
from leezy.assists import TreeContext

class Q099(Solution):
    @solution
    def recoverTree(self, root):
        # 56ms / 68ms
        self.order = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.order.append(node)
            inorder(node.right)
        inorder(root)
        inv = []
        for i in range(1, len(self.order)):
            if self.order[i].val < self.order[i-1].val:
                inv.append(self.order[i-1])
                inv.append(self.order[i])
        if len(inv) == 2:
            n1, n2 = inv[0], inv[1]
        elif len(inv) == 4:
            n1, n2 = inv[0], inv[3]
        n1.val, n2.val = n2.val, n1.val
        return root
    
    @solution
    def recover(self, root):
        # 48ms 90.40%
        self.prev = None
        inv = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev and node.val < self.prev.val:
                inv.append(self.prev)
                inv.append(node)
            self.prev = node
            inorder(node.right)
        inorder(root)
        if len(inv) == 2:
            n1, n2 = inv[0], inv[1]
        elif len(inv) == 4:
            n1, n2 = inv[0], inv[3]
        n1.val, n2.val = n2.val, n1.val
        return root



def main():
    q = Q099()
    q.set_context(TreeContext)
    q.add_args([1, 3, None, None, 2])
    q.add_args([3, 1, 4, None, None, 2])
    q.run()


if __name__ == "__main__":
    main()
