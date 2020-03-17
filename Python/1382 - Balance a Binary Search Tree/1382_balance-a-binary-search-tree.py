from leezy import solution, Solution
from leezy.assists import TreeContext, TreeNode

class Q1382(Solution):
    @solution
    def balanceBST(self, root):
        vals = []
        def collect(node):
            if node is None:
                return
            collect(node.left)
            vals.append(node.val)
            collect(node.right)
        collect(root)

        def build(i, j):
            if i > j:
                return None
            m = i + (j - i) // 2
            node = TreeNode(vals[m])
            node.left = build(i, m-1)
            node.right = build(m+1, j)
            return node
        return build(0, len(vals)-1)


def main():
    q = Q1382()
    q.set_context(TreeContext)
    make = TreeNode.make_tree
    q.add_case(q.case([1, None, 2, None, 3, None, 4, None, None])
                .assert_equal(make([2, 1, 3, None, None, None, 4])))
    q.add_case(q.case([]).assert_equal(make([])))
    q.run()


if __name__ == '__main__':
    main()
