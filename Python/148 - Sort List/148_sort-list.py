from leeyzer import solution, Solution
from leeyzer.assists import LinkedListNode, LinkedListContext


class Q148(Solution):
    @solution
    def sortList(self, head):
        def merge(s1, s2):
            dummy = LinkedListNode()
            tail = dummy
            while s1 and s2:
                if s1.val <= s2.val:
                    tail.next = s1
                    tail = s1
                    s1 = s1.next
                else:
                    tail.next = s2
                    tail = s2
                    s2 = s2.next
            tail.next = s1 or s2
            return dummy.next
        if head is None or head.next is None:
            return head
        prev = head
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        s1 = self.sortList(head)
        s2 = self.sortList(slow)
        return merge(s1, s2)



def main():
    q = Q148()
    q.set_context(LinkedListContext)
    q.add_args([4])
    q.add_args([4, 2])
    q.add_args([2, 4])
    q.add_args([4, 2, 1, 3])
    q.add_args([-1, 5, 3, 4, 0])
    q.run()

if __name__ == '__main__':
    main()
