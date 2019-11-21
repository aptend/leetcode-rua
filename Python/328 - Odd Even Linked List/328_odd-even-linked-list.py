from leezy import solution, Solution
from leezy.assists import LinkedListContext

class Q328(Solution):
    @solution
    def oddEvenList(self, head):
        # 40ms
        if not head or not head.next:
            return head
        ot = head
        even = et = head.next
        node = head.next.next
        i = 0
        while node:
            if i % 2 == 0:
                ot.next = node
                ot = node
            else:
                et.next= node
                et = node
            i += 1
            node = node.next
        ot.next = even
        et.next = None
        return head

    @solution
    def odd_even_list(self, head):
        # 36ms
        if head is None:
            return None
        odd_t = head
        even_h = even_t = head.next
        while even_t and even_t.next:
            odd_t.next = even_t.next
            odd_t = even_t.next
            tmp = even_t.next.next
            even_t.next = tmp
            even_t = tmp
        odd_t.next = even_h
        return head



def main():
    q = Q328()
    q.set_context(LinkedListContext)
    q.add_case(q.case([1, 2, 3, 4, 5]))
    q.add_case(q.case([1, 2, 3]))
    q.run()

if __name__ == '__main__':
    main()
