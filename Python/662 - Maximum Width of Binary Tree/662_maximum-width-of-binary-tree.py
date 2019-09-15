from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q662(Solution):
    @solution
    def widthOfBinaryTree(self, root):
        # 24ms 76.16%
        if root is None:
            return 0
        ans = 1
        level = [(root, 1)]
        while level:
            nxt = []
            for node, pos in level:
                if node.left:
                    nxt.append((node.left, pos*2-1))
                if node.right:
                    nxt.append((node.right, pos*2))
            if len(nxt) > 1:
                ans = max(ans, nxt[-1][1] - nxt[0][1] + 1)
            level = nxt
        return ans


def main():
    q = Q662()
    q.set_context(TreeContext)
    q.add_args([1, 3, 2, 5, 3, None, 9])
    q.add_args([1, 1, 1, 1, None, None, 1, 1, None, None, 1])
    q.run()


if __name__ == "__main__":
    main()
