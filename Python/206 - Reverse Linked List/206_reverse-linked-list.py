from leezy import solution, Solution
from leezy.assists import LinkedListContext, LinkedListNode

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
    def reverse_iter(self, head):
        dummy = LinkedListNode()
        while head:
            nxt = head.next
            head.next = dummy.next
            dummy.next = head
            head = nxt
        return dummy.next

    @solution
    def reverse_iter_nodummy(self, head):
        if not head:
            return
        new_head = head
        head = head.next
        new_head.next = None
        while head:
            nxt_handle = head.next
            head.next = new_head
            new_head = head
            head = nxt_handle
        return new_head


def main():
    q = Q206()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.add_case(q.case([1]))
    q.add_case(q.case([]))
    q.run()

if __name__ == '__main__':
    main()
