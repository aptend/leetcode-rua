from leezy import solution, Solution
from leezy.assists import TreeContext

from collections import deque

class Q199(Solution):
    @solution
    def rightSideView(self, root):
        # 32ms
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n-1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
    
    @solution
    def right_side_view(self, root):
        # 28ms 82.50%
        ans = []
        def walk(node, lv):
            if node is None:
                return
            if lv > len(ans):
                ans.append(node.val)
            else:
                ans[lv-1] = node.val
            walk(node.left, lv+1)
            walk(node.right, lv+1)
        walk(root, 1)
        return ans


def main():
    q = Q199()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, None, 5, None, 4]).assert_equal([1, 3, 4]))
    q.run()

if __name__ == '__main__':
    main()
