

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        # 36ms 94.73%
        # O(n) space
        if not head:
            return None
        links = dict()
        p = head
        dummy_h = dummy_t = Node('_', None, None)
        while p:
            cpy_p = Node(p.val, None, None)
            dummy_t.next = cpy_p
            dummy_t = cpy_p
            links[p] = cpy_p
            p = p.next

        p = head
        q = dummy_h.next
        while p:
            if p.random:
                q.random = links[p.random]
            p = p.next
            q = q.next
        return dummy_h.next

    def copy_list(self, head):
        # 44ms
        if not head:
            return None

        # modify original linkedlist to record mapping between node and copied node
        p = head
        while p:
            cpy_p = Node(p.val, p.next, None)
            p.next = cpy_p
            p = cpy_p.next

        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            # iters on original nodes
            p = p.next.next

        # pick all copied nodes and restore original linkedlist
        copy_h = prev = head.next
        head.next = head.next.next
        p = head.next # start from 2nd node of original linkedlist
        while p:
            prev.next = p.next
            prev = p.next
            p.next = p.next.next
            p = p.next

        return copy_h


def main():
    pass


if __name__ == '__main__':
    main()
