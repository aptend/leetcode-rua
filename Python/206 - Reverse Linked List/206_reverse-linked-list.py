from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode


class Q206(Solution):
    @solution
    def reverseList(self, head):
        def reverse(node):
            if not node.next:
                return node, node
            h, t = reverse(node.next)
            t.next = node
            node.next = None
            return h, node

        if not head or not head.next:
            return head
        h, _ = reverse(head)
        return h

    @solution
    def rev(self, head):
        if head is None or head.next is None:
            return head
        rev_list = self.rev(head.next)
        head.next.next = head
        head.next = None
        return rev_list

    @solution
    def reverse_iter(self, head):
        dummy = ListNode()
        while head:
            nxt = head.next
            head.next = dummy.next
            dummy.next = head
            head = nxt
        return dummy.next

    @solution
    def reverse_iter_no_dummy(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev


def main():
    q = Q206()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.add_case(q.case([1]))
    q.add_case(q.case([]))
    q.run()


if __name__ == '__main__':
    main()
