from leezy import solution, Solution
from leezy.assists import LinkedListNode

class Q061(Solution):
    @solution
    def rotateRight(self, head, k):
        # 48ms 23.51%
        if head is None:
            return
        n = 0
        node = head
        tail = None
        while node:
            n += 1
            tail = node
            node = node.next

        k = n - k % n
        if k == n:
            return head
        
        node = head
        while k > 1:
            k -= 1
            node = node.next
        new_head = node.next
        node.next = None
        tail.next = head
        return new_head



def main():
    q = Q061()
    q.add_args(LinkedListNode.make_linked_list([1, 2, 3, 4, 5]), 2)
    q.add_args(LinkedListNode.make_linked_list([1, 2, 3, 4, 5]), 0)
    q.add_args(LinkedListNode.make_linked_list([]), 0)
    q.run()

if __name__ == '__main__':
    main()
