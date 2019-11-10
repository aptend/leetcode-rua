from leezy import Solution, solution


class Q109(Solution):
    @solution
    def sortedListToBST(self, head):
        # 104ms 97.16%
        A = []
        while head:
            A.append(head.val)
            head = head.next

        def construct(i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(A[i])
            mid = i + (j-i) // 2
            node = TreeNode(A[mid])
            node.left = construct(i, mid-1)
            node.right = construct(mid+1, j)
            return node
        return construct(0, len(A)-1)


def main():
    q = Q109()
    q.add_args([-10, -3, 0, 5, 9])
    q.run()


if __name__ == "__main__":
    main()
