from leeyzer import solution, Solution
from leeyzer.assists import LinkedListNode

class Q141(Solution):
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
    new = LinkedListNode.make_linked_list
    link = LinkedListNode.make_circle_list
    q.add_args(link(new([3, 2, 0, -4]), 1))
    q.add_args(link(new([3, 2, 0, -4]), -1))
    q.run()

if __name__ == '__main__':
    main()
