from leezy import Solution, solution
from leezy.assists import TreeContext


class Q113(Solution):
    @solution
    def pathSum(self, root, sum):
        # 36ms 73.27% 
        current, total = [], []
        if root is None:
            return []
        self.dfs(root, sum, current, total)
        return total

    def dfs(self, node, target, current, total):
        if not node.left and not node.right:
            if node.val == target:
                total.append(current[:]+[node.val])
            return
        if node.left:
            current.append(node.val)
            self.dfs(node.left, target-node.val, current, total)
            current.pop()
        if node.right:
            current.append(node.val)
            self.dfs(node.right, target-node.val, current, total)
            current.pop()



def main():
    q = Q113()
    q.set_context(TreeContext)
    q.add_args([5, 4, 8], 2)
    q.add_args([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22)
    q.run()


if __name__ == "__main__":
    main()
