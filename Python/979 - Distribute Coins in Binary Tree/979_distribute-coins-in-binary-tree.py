from leeyzer import Solution, solution
from leeyzer.assists import TreeContext


class Q979(Solution):
    @solution
    def distributeCoins(self, root):
        self.ans = 0
        self.travel(root)
        return self.ans
    
    def travel(self, node):
        if node is None:
            return 0
        l = self.travel(node.left)
        r = self.travel(node.right)
        self.ans += abs(l) + abs(r)
        return node.val - 1 + l + r


def main():
    q = Q979()
    q.set_context(TreeContext)
    q.add_args([3, 0, 0])
    q.add_args([0, 3, 0])
    q.add_args([1, 0, 2])
    q.add_args([1, 0, 0, None, 3])
    q.run()


if __name__ == "__main__":
    main()
