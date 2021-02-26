from leezy import Solution, solution
from leezy.assists import TreeContext, TreeNode


class Q426(Solution):
    @solution
    def convert_search_BST(self, root):
        if root is None:
            return None
        l_head = self.convert_search_BST(root.left)
        r_head = self.convert_search_BST(root.right)
        if l_head:  # append current node to left linked list
            l_tail = l_head.left
            root.left = l_tail
            root.right = l_head
            l_tail.right = root
            l_head.left = root
        else:  # make current node become the left linked list
            root.left = root
            root.right = root
            l_head = root
        if r_head:  # link left and right list
            l_tail = l_head.left
            r_tail = r_head.left
            l_tail.right = r_head
            r_head.left = l_tail
            r_tail.right = l_head
            l_head.left = r_tail
        return l_head

    @solution
    def convert(self, root):
        if root is None:
            return
        dummy = TreeNode('^')
        self.tail = dummy
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.tail.right = node
            node.left = self.tail
            self.tail = node
            inorder(node.right)
        inorder(root)
        dummy.right.left = self.tail
        self.tail.right = dummy.right
        return dummy.right


def main():
    q = Q426()
    q.set_context(TreeContext)
    from functools import partial

    def check_double(head, vals):
        print(vals)
        N = len(vals)
        node = head
        for i in range(N):
            if node.val != vals[i]:
                return False
            node = node.right
        node = head.left
        for i in range(N-1, -1, -1):
            if node.val != vals[i]:
                return False
            node = node.left
        return True
    
    # Be careful. if the test failed, the program will loop forever, trying to 
    # formt the result of converted tree, which is a invalid tree.
    q.add_case(q.case([4, 2, 7, 1, 3])
                .assert_true_with(partial(check_double, vals=[1, 2, 3, 4, 7])))
    q.run()


if __name__ == "__main__":
    main()
