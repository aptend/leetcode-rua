from leeyzer import solution, Solution

class Q160(Solution):
    @solution
    def getIntersectionNode(self, headA, headB):
        # 224ms
        A, B = headA, headB
        while A is not B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
    
    @solution
    def get_intersection(self, headA, headB):
        # 200ms
        pool = set()
        while headA:
            pool.add(headA)
            headA = headA.next

        while headB:
            if headB in pool:
                return headB
            headB = headB.next
        return None

def main():
    q = Q160()
    q.add_args(8, [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3)
    q.run()

if __name__ == '__main__':
    main()
