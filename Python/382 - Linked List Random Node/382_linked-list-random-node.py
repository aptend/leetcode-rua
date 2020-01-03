from leezy.assists import LinkedListNode
from random import randint


class Q382:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        picked = None
        node = self.head
        pos = 0
        while node:
            if randint(0, pos) == 0:
                picked = node.val
            pos += 1
            node = node.next
        return picked


def main():
    q = Q382(LinkedListNode.make_linked_list([1, 2, 3, 4, 5]))
    print([q.getRandom() for _ in range(10)])


if __name__ == '__main__':
    main()
