from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode


class Q143(Solution):
    @solution
    def reorderList(self, head):
        # 96ms 50.22%
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half2 = ListNode()
        node = slow.next  # this point is tricky, be careful
        slow.next = None
        while node:
            next_node = node.next
            node.next = half2.next
            half2.next = node
            node = next_node
        ans = ListNode()
        dummy = ans
        half1 = head
        half2 = half2.next
        while half2:
            ans.next = half1
            half1 = half1.next
            ans.next.next = half2
            ans = half2
            half2 = half2.next
        ans.next = half1
        return dummy.next


def main():
    q = Q143()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4]))
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.add_case(q.case([]))
    q.add_case(q.case([1, 2]))
    q.add_case(q.case([1]))
    q.run()

if __name__ == '__main__':
    main()
