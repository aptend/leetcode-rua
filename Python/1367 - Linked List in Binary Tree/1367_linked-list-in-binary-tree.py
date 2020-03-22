from leezy import solution, Solution
from leezy.assists import TreeNode, ListNode

class Q1367(Solution):
    def compare(self, lnode, tnode):
        if lnode is None:
            return True
        elif tnode:
            if lnode.val == tnode.val:
                return self.compare(lnode.next, tnode.right) or \
                       self.compare(lnode.next, tnode.left)
            else:
                return False
        return False

    @solution
    def isSubPath(self, head, root):
        if self.compare(head, root):
            return True
        if root:
            return self.isSubPath(head, root.left) or \
                   self.isSubPath(head, root.right)
        return False


def main():
    q = Q1367()
    mkl = ListNode.make_linked_list
    mkt = TreeNode.make_tree
    q.add_case(q.case(
        mkl([4, 2, 8]),
        mkt([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))
    q.add_case(q.case(
        mkl([1, 4, 2, 6, 8]),
        mkt([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    ))
    q.run()


if __name__ == '__main__':
    main()
