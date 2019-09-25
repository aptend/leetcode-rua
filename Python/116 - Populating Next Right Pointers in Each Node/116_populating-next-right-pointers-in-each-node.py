# unrecoginzed solution pattern, leave it on your own


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_iter_linear_space(self, root):
        # 64ms 92.43%
        if root is None:
            return None
        cur_lvl = [root, None]
        nxt_lvl = []
        while True:
            for i, node in enumerate(cur_lvl[:-1]):
                node.next = cur_lvl[i+1]
                if node.left:
                    nxt_lvl.append(node.left)
                    nxt_lvl.append(node.right)
            if len(nxt_lvl) == 0:
                break
            nxt_lvl.append(None)
            cur_lvl, nxt_lvl = nxt_lvl, cur_lvl
            nxt_lvl.clear()
        return root

    def connect_iter_constant_space(self, root):
        # 60ms 98.54%
        node = root
        dummy = tail = Node(-42, None, None, None)
        while node and node.left:
            tail.next = node.left
            tail = tail.next
            tail.next = node.right
            tail = tail.next
            # we have reached the end of this level
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next  # move to next level
        return root

    def connect_preorder(self, root):
        # 76ms
        if root is None or root.left is None:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect_preorder(root.left)
        self.connect_preorder(root.right)
        return root
    
    def connect_postorder(self, root):
        # 72ms
        # time complexity could be inferred by Akra–Bazzi theorem
        # approximately linear
        def link_tree(node1, node2):
            while node1 and node2:
                node1.next = node2
                node1 = node1.right
                node2 = node2.left

        if root is None:
            return None
        left = self.connect_postorder(root.left)
        right = self.connect_postorder(root.right)
        link_tree(left, right)



def main():
    pass

if __name__ == "__main__":
    main()
