from leezy import solution, Solution
from leezy.assists import TreeContext


class Q114(Solution):
    @solution
    def flatten(self, root):
        # 32ms 96.44%
        def _flat(node):
            if not node:
                return None
            lf = _flat(node.left)
            rf = _flat(node.right)
            if lf is None and rf is None:
                return node, node
            elif lf is None:
                node.right = rf[0]
                node.left = None
                return node, rf[1]
            elif rf is None:
                node.right = lf[0]
                node.left = None
                return node, lf[1]
            else:
                node.right = lf[0]
                node.left = None
                lf[1].right = rf[0]
                return node, rf[1]
        return _flat(root)[0]


def main():
    q = Q114()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 5, 3, 4, None, 6]))
    q.add_case(q.case([1, 2]))
    q.run()


if __name__ == '__main__':
    main()
