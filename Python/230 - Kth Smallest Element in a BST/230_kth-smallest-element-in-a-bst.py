from leezy import solution, Solution
from leezy.assists import TreeContext


class Q230(Solution):
    @solution
    def kthSmallest(self, root, k):
        # same idea for follow up question, maintain how many chidren nodes
        self.mark(root)
        return self.find(root, k)

    def find(self, node, i):
        if node.left_cnt > i - 1:
            return self.find(node.left, i)
        elif node.left_cnt < i - 1:
            return self.find(node.right, i-node.left_cnt-1)
        else:
            return node.val

    def mark(self, node):
        if node is None:
            return 0
        node.left_cnt = self.mark(node.left)
        node.right_cnt = self.mark(node.right)
        return node.left_cnt + node.right_cnt + 1


def main():
    q = Q230()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 1, 4, None, 2], 1).assert_equal(1))
    q.add_case(q.case([5, 3, 6, 2, 4, None, None, 1], 3).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
