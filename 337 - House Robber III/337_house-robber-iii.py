from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q337(Solution):
    @solution
    def rob(self, root):
        # 36ms 48ms
        memo = {}
        def _rob(node):
            if node is None:
                return 0
            if node in memo:
                return memo[node]
            ll = lr = rl = rr = 0
            if node.left: 
                ll = _rob(node.left.left)
                lr = _rob(node.left.right)
            if node.right: 
                rl = _rob(node.right.left)
                rr = _rob(node.right.right)
            rob_node = node.val + ll + lr + rl + rr
            not_rob_node = _rob(node.left) + _rob(node.right)
            val = max(rob_node, not_rob_node)
            memo[node] = val
            return val
        return _rob(root)

    @solution
    def rob_tuple(self, root):
        # 24ms 99.41%  40ms 48ms
        def rob_(node):
            if node is None:
                return 0, 0
            # a subtree rooting at node.left
            # l: maximum with robbing node.left
            # nol: maximum without robbing node.left 
            l, nol = rob_(node.left)
            r, nor = rob_(node.right)
            return node.val + nol + nor, max(l, nol) + max(r, nor)
        return max(rob_(root))
            



def main():
    q = Q337()
    q.set_context(TreeContext)
    q.add_args([3, 2, 3, None, 3, None, 1])  # 7
    q.add_args([3, 4, 5, 1, 3, None, 1])  # 9
    q.add_args([4, 1, None, 2, None, 3])  # 7
    q.run()


if __name__ == "__main__":
    main()
