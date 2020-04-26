from leezy import solution, Solution
from leezy.assists import LinkedListContext, ListNode


class Q019(Solution):
    @solution
    def removeNthFromEnd(self, head, n):
        # 32ms 89%
        dummy = ListNode(0)
        dummy.next = head
        node = scout = dummy
        for _ in range(n+1):
            scout = scout.next
        while scout:
            node = node.next
            scout = scout.next

        node.next = node.next.next
        return dummy.next


def main():
    q = Q019()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1], 1))
    q.add_case(q.case([1, 2], 2))
    q.add_case(q.case([1, 2, 3, 4, 5], 2))
    q.run()

if __name__ == '__main__':
    main()
