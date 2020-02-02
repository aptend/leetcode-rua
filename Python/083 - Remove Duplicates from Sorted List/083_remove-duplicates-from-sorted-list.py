from leezy import solution, Solution
from leezy.assists import LinkedListContext, LinkedListNode


class Q083(Solution):
    @solution
    def deleteDuplicates(self, head):
        # 32ms 97.06%
        dummy = LinkedListNode(float('inf'))
        dummy.next = head
        prev = dummy
        while head:
            if prev.val != head.val:
                prev.next = head
                prev = head
            head = head.next
        prev.next = None
        return dummy.next


def main():
    q = Q083()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 1, 2]))
    q.add_case(q.case([1, 1, 2, 3, 3]))
    q.add_case(q.case([]))
    q.run()

if __name__ == '__main__':
    main()
