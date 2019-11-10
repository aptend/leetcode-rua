from collections import deque

from leezy import Solution, solution
from leezy.assists import TreeContext

class Q111(Solution):
    @solution
    def minDepth(self, root):
        # 32ms 80.25%
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        cnt = 0
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return cnt
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return -1 # can't reach here
    
    @solution
    def min_depth(self, root):
        # 40ms
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + self.min_depth(root.right)
        elif root.right is None:
            return 1 + self.min_depth(root.left)
        else:
            return 1+ min(self.min_depth(root.left),
                          self.min_depth(root.right))



def main():
    q = Q111()
    q.set_context(TreeContext)
    q.add_args([3, 9, 20, None, None, 15, 7])
    q.add_args([1, None, 2])
    q.run()


if __name__ == "__main__":
    main()
