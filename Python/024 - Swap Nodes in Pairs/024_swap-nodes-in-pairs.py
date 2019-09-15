from leeyzer import Solution, solution
from leeyzer.assists import LinkedListContext, ListNode

class Q024(Solution):
    @solution
    def swapPairs(self, head):
        # 12ms 95.04% / 20ms
        dummy = ListNode(42)
        dummy.next = head
        prev = dummy
        while True:
            if head is None or head.next is None:
                break
            after = head.next.next
            prev.next = head.next
            prev.next.next = head
            head.next = after
            prev = head
            head = after
        return dummy.next


def main():
    q = Q024()
    q.set_context(LinkedListContext)
    q.add_args([1])
    q.add_args([1, 2, 3])
    q.add_args([1, 2, 3, 4])
    q.run()


if __name__ == "__main__":
    main()
