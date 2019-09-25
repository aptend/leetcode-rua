# unrecoginzed solution pattern, leave it on your own


class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        # 388ms 77.87%
        if not root:
            return
        if root.left and root.right:
            root.left.next = root.right

        if root.next and root.left or root.right:
            left_op = root.right or root.left
            node = root.next
            # follow this level to find possible right_op
            while node:
                right_op = node.left or node.right
                if right_op:
                    left_op.next = right_op
                    break
                node = node.next
        # connect right first
        self.connect(root.right)
        self.connect(root.left)
        return root
    
    def connect_constant_space(self, root):
        # 388ms
        node = root
        dummy = tail = Node(-42, None, None, None)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            # we have reached the end of this level
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next  # move to next level
        return root



def main():
    pass

if __name__ == "__main__":
    main()
