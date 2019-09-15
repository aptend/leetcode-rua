from collections import deque

from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q107(Solution):
    @solution
    def levelOrderBottom(self, root):
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans[::-1]


def main():
    q = Q107()
    q.set_context(TreeContext)
    q.add_args([3, 9, 20, None, None, 15, 7])
    q.run()


if __name__ == "__main__":
    main()
