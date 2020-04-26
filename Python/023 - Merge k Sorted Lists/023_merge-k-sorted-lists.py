from leezy import solution, Solution

from leezy.assists import ListNode
from heapq import heappop, heappush

class Q023(Solution):

    def merge(self, s1, s2):
        dummy = ListNode()
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

    @solution
    def mergeKLists(self, lists):
        # 124ms
        n = len(lists)
        while n > 1:
            for i in range(0, n, 2):
                if i == n - 1:
                    lists[i//2] = lists[i]
                else:
                    lists[i//2] = self.merge(lists[i], lists[i+1])
            n = (n+1) // 2
        return lists[0] if lists else None
    
    @solution
    def merge_lists(self, lists):
        # 108ms 89.38%
        heap = []
        for i, l in enumerate(lists):
            if not l:
                continue
            heappush(heap, (l.val, i, l))
            lists[i] = l.next
        dummy = tail = ListNode()
        while heap:
            _, i, node = heappop(heap)
            tail.next, tail = node, node
            if lists[i]:
                nxt = lists[i]
                heappush(heap, (nxt.val, i, nxt))
                lists[i] = nxt.next
        return dummy.next




def main():
    q = Q023()
    q.add_args([])
    q.add_args([
        ListNode.make_linked_list([1, 4, 5]), 
        ListNode.make_linked_list([1, 3, 4]),
        ListNode.make_linked_list([2, 6])])
    q.run()

if __name__ == '__main__':
    main()
