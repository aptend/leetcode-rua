from leeyzer import Solution, solution
from leeyzer.assists import LinkedListContext, ListNode


class Q147(Solution):
    @solution
    def insertionSortList(self, head):
        dummy = ListNode(42)
        dummy.next = head
        tail = head
        while head:
            node = dummy
            while node.next.val < head.val:
                node = node.next
            if node.next is head:
                tail = head
                head = head.next
            else:
                after = head.next
                tail.next = after
                head.next = node.next
                node.next = head
                head = after
        return dummy.next


def main():
    q = Q147()
    q.set_context(LinkedListContext)
    q.add_args([2])
    q.add_args([4, 2, 1, 3, 2])
    q.add_args([5, 4, 3, 2, 1])
    q.run()


if __name__ == "__main__":
    main()
