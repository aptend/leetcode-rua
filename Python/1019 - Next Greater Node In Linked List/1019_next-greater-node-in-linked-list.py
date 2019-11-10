from leezy import Solution, solution
from leezy.assists import LinkedListContext


class Q1019(Solution):
    @solution
    def nextLargerNodes(self, head):
        # 348ms 59.82%
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        N = len(nums)
        ans = [0] * N
        stack = []
        for i in range(N-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(nums[i])
        return ans


def main():
    q = Q1019()
    q.set_context(LinkedListContext)
    q.add_args([2, 1, 5])
    q.add_args([3, 3])
    q.run()


if __name__ == "__main__":
    main()
