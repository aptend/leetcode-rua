from leeyzer import solution, Solution
from leeyzer.assists import LinkedListContext, LinkedListNode

class Q206(Solution):
    @solution
    def reverseList(self, head):
        def reverse(node):
            if not node.next:
                return node, node
            h, t = reverse(node.next)
            t.next = node
            node.next = None
            return h, node

        if not head or not head.next:
            return head
        h, _ = reverse(head)
        return h

    @solution
    def reverse_iter(self, head):
        dummy = LinkedListNode()
        while head:
            nxt = head.next
            head.next = dummy.next
            dummy.next = head
            head = nxt
        return dummy.next




def main():
    q = Q206()
    q.set_context(LinkedListContext)
    q.add_args([1, 2, 3, 4, 5])
    q.add_args([1])
    q.add_args([])
    q.run()

if __name__ == '__main__':
    main()
