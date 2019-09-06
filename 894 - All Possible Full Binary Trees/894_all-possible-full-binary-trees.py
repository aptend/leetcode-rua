from leeyzer import Solution, solution
from leeyzer.assists import TreeNode
from functools import lru_cache

class Q894(Solution):
    @solution
    def allPossibleFBT(self, N):
        # 164ms 53.50%
        @lru_cache(maxsize=N*N)
        def construct(i, j):
            if i == j:
                return [TreeNode(0)]
            ans = []
            for k in range(i+1, j):
                left = construct(i, k-1)
                right = construct(k+1, j)
                for l in left:
                    for r in right:
                        node = TreeNode(0)
                        node.left = l
                        node.right = r
                        ans.append(node)
            return ans
        return construct(0, N-1)


def main():
    q = Q894()
    q.add_args(1)
    q.add_args(2)
    q.run()
    for t in q.allPossibleFBT(7):
        print(t)


if __name__ == "__main__":
    main()
