from leeyzer import Solution, solution
from leeyzer.assists import TreeContext
from collections import deque

class Q102(Solution):
    @solution
    def levelOrder(self, root):
        # 12ms 99.29%
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
        return ans
    
    @solution
    def level_order_dfs(self, root):
        # 20ms
        ans = []
        def dfs(node, depth):
            if node is None:
                return
            if len(ans) <= depth:
                ans.append([])
            ans[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return ans



def main():
    q = Q102()
    q.set_context(TreeContext)
    q.add_args([3, 9, 20, None, None, 15, 7])
    q.run()


if __name__ == "__main__":
    main()
