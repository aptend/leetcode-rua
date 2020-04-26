from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode

class Q025(Solution):
    @solution
    def reverseKGroup(self, head, k):
        # 48ms 69.25%
        if head is None or k == 1:
            return head
        dummy = ListNode('^')
        dummy.next = head
        n = 0
        while head:
            n += 1
            head = head.next

        prev_block_tail = dummy
        node = dummy.next
        for _ in range(n // k):
            # reverse k nodes
            inner_head = node
            inner_tail = node
            node = node.next
            for _ in range(k-1):
                next_to_handle = node.next
                node.next = inner_head
                inner_head = node
                node = next_to_handle
            # take k nodes into the whole chain
            prev_block_tail.next = inner_head
            prev_block_tail = inner_tail
            inner_tail.next = node
        return dummy.next



def main():
    q = Q025()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4, 5], 2))
    q.add_case(q.case([1, 2, 3, 4, 5], 3))
    q.run()

if __name__ == '__main__':
    main()
