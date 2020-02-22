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
                total.append(current+[node.val])
            return
        current.append(node.val)
        if node.left:
            self.dfs(node.left, target-node.val, current, total)
        if node.right:
            self.dfs(node.right, target-node.val, current, total)
        current.pop()



def main():
    q = Q113()
    q.set_context(TreeContext)
    q.add_case(q.case([5, 4, 8], 2).assert_equal([]))
    q.add_case(q.case([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22)
                .assert_equal([[5, 4, 11, 2], [5, 8, 4, 5]]))
    q.run()


if __name__ == "__main__":
    main()
