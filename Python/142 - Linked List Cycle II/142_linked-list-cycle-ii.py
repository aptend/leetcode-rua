from leezy import solution, Solution
from leezy.assists import ListNode


class Q142(Solution):
    @solution
    def detectCycle(self, head):
        # 32ms 96.97%
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        else:
            return None

        cursor = head
        while cursor is not slow:
            cursor = cursor.next
            slow = slow.next
        print(cursor.val)
        return cursor


def main():
    q = Q142()
    make = ListNode.make_cycle_list

    def check_val(val):
        return lambda node: node.val == val
    q.add_case(q.case(make([3, 2, 0, -4], 1)).assert_true_with(check_val(2)))
    q.add_case(q.case(make([1, 2], 0)).assert_true_with(check_val(1)))
    q.add_case(q.case(make([1], -1)).assert_equal(None))
    q.run()


if __name__ == '__main__':
    main()
