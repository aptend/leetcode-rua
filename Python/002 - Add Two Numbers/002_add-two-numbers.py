from leezy import solution, Solution
from leezy.assists import LinkedListContext, LinkedListNode


class Q002(Solution):
    @solution
    def addTwoNumbers(self, l1, l2):
        # 84ms
        carry = 0
        dummy = LinkedListNode()
        tail = dummy
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next

            if l2:
                s += l2.val
                l2 = l2.next

            carry, v = divmod(s + carry, 10)
            tail.next = LinkedListNode(v)
            tail = tail.next
        if carry:
            tail.next = LinkedListNode(carry)
        return dummy.next


def main():
    q = Q002()
    q.set_context(LinkedListContext)
    make = LinkedListNode.make_linked_list
    q.add_case(q.case([2, 4, 3], [5, 6, 4])
                .assert_equal(make([7, 0, 8])))
    q.add_case(q.case([2, 4, 3, 1], [5, 6, 4])
                .assert_equal(make([7, 0, 8, 1])))
    q.add_case(q.case([5], [5])
                .assert_equal(make([0, 1])))
    q.add_case(q.case([1], [9, 9, 9, 9])
                .assert_equal(make([0, 0, 0, 0, 1])))
    q.run()


if __name__ == '__main__':
    main()
