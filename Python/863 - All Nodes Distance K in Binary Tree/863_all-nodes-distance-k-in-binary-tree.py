from leeyzer import Solution, solution
from leeyzer.assists import TreeNode

class Q863(Solution):
    @solution
    def distanceK(self, root, target, K):
        # 44ms 73.92%
        def add_p(node, par):
            if not node:
                return
            node.par = par
            add_p(node.left, node)
            add_p(node.right, node)

        add_p(root, None)
        seen = set()
        self.ans = []
        def collect(node, n):
            if not node or n < 0:
                return
            if n == 0:
                self.ans.append(node.val)
                return
            if node.left not in seen:
                collect(node.left, n-1)
            if node.right not in seen:
                collect(node.right, n-1)

        n = K
        node = target
        while node and n >= 0:
            collect(node, n)
            seen.add(node)
            n -= 1
            node = node.par

        return self.ans

def main():
    q = Q863()
    t1 = TreeNode.make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    q.add_args(t1, t1.left, 2)

    t2 = TreeNode.make_tree([0, 2, 1, None, None, 3])
    q.add_args(t2, t2.right.left, 3)
    q.run()


if __name__ == "__main__":
    main()
