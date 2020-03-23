from leezy import solution, Solution
from leezy.assists import LinkedListContext


class Q876(Solution):
    @solution
    def middleNode(self, head):
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def mid_node(self, head):
        # return the first middle node
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        return slow


def main():
    q = Q876()

    def check_val(n):
        return lambda x: x.val == n

    q.set_context(LinkedListContext)
    q.add_case(q.case([1]).assert_true_with(check_val(1)))
    q.add_case(q.case([1, 2]).assert_true_with(check_val(2)))
    q.add_case(q.case([1, 2, 3]).assert_true_with(check_val(2)))
    q.add_case(q.case([1, 2, 3, 4]).assert_true_with(check_val(3)))
    q.add_case(q.case([1, 2, 3, 4, 5]).assert_true_with(check_val(3)))
    q.run()


if __name__ == '__main__':
    main()
