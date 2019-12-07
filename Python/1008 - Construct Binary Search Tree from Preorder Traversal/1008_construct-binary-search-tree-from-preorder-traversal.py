from leezy import solution, Solution
from leezy.assists import TreeNode

class Q1008(Solution):
    @solution
    def bstFromPreorder(self, preorder):
        # 32ms 93,79%
        def make(i, j):
            if i > j:
                return None
            v = preorder[i]
            node = TreeNode(v)
            k = i + 1
            while k <= j and preorder[k] < v:
                k += 1
            node.left = make(i+1, k-1)
            node.right = make(k, j)
            return node
        return make(0, len(preorder)-1)


def main():
    q = Q1008()
    q.add_case(q.case([8, 5, 1, 7, 10, 12]))
    q.run()

if __name__ == '__main__':
    main()
