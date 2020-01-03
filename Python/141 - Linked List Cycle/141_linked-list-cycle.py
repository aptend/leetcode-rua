from leezy import solution, Solution
from leezy.assists import LinkedListNode


class Q141(Solution):
    @solution
    def has_cycle(self, head):
        # 56ms 75.68% more concise than the old version
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False

    @solution
    def hasCycle(self, head):
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


def main():
    q = Q141()
    make = LinkedListNode.make_cycle_list

    q.add_case(q.case(make([3, 2, 0, -4], 1)).assert_equal(True))
    q.add_case(q.case(make([1, 2], 0)).assert_equal(True))
    q.add_case(q.case(make([1], -1)).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
