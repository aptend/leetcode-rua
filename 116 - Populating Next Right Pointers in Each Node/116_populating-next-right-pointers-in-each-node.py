# unrecoginzed solution pattern, leave it on your own


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_iter(self, root):
        """
        :type root: Node
        :rtype: Node
        """
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

    def connect_recur(self, root):
        # 76ms
        if root is None or root.left is None:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect_recur(root.left)
        self.connect_recur(root.right)
        return root


def main():
    pass

if __name__ == "__main__":
    main()
