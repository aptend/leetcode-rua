from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q987(Solution):
    @solution
    def verticalTraversal(self, root):
        # 8ms 99.84%
        vals = []
        def position_val(node, x, y):
            if node is None:
                return
            vals.append((x, y, node.val))
            position_val(node.left, x-1, y+1)
            position_val(node.right, x+1, y+1)
        position_val(root, 0, 0)
        last_x = -10000
        ans = []
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)
        return ans


    def vertical_no_order(self, root):
        def span(node):
            if node is None:
                return -1, -1
            ll, lr = span(node.left)
            rl, rr = span(node.right)
            return max(ll+1, rl-1), max(lr-1, rr+1)
        lspan, rspan = span(root)

        ans = [[] for _ in range(lspan+rspan+1)]

        def collect(node, offset):
            if node is None:
                return
            ans[offset].append(node.val)
            collect(node.left, offset - 1)
            collect(node.right, offset + 1)
        collect(root, lspan)
        return ans



def main():
    q = Q987()
    q.set_context(TreeContext)
    q.add_args([])
    q.add_args([42])
    q.add_args([3, 9, 20, None, None, 15, 7])
    q.add_args([1, 2, 3, 4, 5, 6, 7])
    q.add_args([0, 8, 1, None, None, 3, 2, None, 4, 5, None, None, 7, 6])
    q.run()


if __name__ == "__main__":
    main()
