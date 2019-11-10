from leezy import solution, Solution

class Q021(Solution):
    @solution
    def mergeTwoLists(self, l1, l2):
        # 20ms 96%
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        tail.next = l1 or l2
        return dummy.next


def main():
    q = Q021()
    q.add_args([1, 2, 4], [1, 3, 4])
    q.run()

if __name__ == '__main__':
    main()
