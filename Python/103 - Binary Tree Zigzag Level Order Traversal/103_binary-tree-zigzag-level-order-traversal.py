from leezy import solution, Solution
from leezy.assists import TreeContext

from collections import deque


class Q103(Solution):
    @solution
    def zigzagLevelOrder(self, root):
        # 32ms 89.68%
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            lv = []
            for _ in range(len(q)):
                node = q.popleft()
                lv.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(ans) % 2 == 1:
                lv.reverse()
            ans.append(lv)
        return ans


def main():
    q = Q103()
    q.set_context(TreeContext)
    q.add_case(q.case([3, 9, 20, None, None, 15, 7]))
    q.run()

if __name__ == '__main__':
    main()
