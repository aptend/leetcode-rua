from leeyzer import Solution, solution
from leeyzer.assists import ListNode


class Q445(Solution):
    @solution
    def addTwoNumbers(self, l1, l2):
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        node = None
        while s1 and s2:
            carry, v = divmod(s1.pop()+s2.pop()+carry, 10)
            n = ListNode(v)
            n.next, node = node, n
        s = s1 or s2
        while s:
            carry, v = divmod(s.pop()+carry, 10)
            n = ListNode(v)
            n.next, node = node, n
        if carry:
            n = ListNode(carry)
            n.next, node = node, n
        return node



def main():
    q = Q445()
    q.add_args(ListNode.make_linked_list([9, 4, 4, 3]),
               ListNode.make_linked_list([5, 6, 4]))
    q.add_args(ListNode.make_linked_list([0]),
               ListNode.make_linked_list([9, 9, 9]))
    q.run()


if __name__ == "__main__":
    main()
