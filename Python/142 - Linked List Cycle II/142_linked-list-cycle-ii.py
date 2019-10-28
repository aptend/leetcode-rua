from leeyzer import solution, Solution

class Q142(Solution):
    @solution
    def detectCycle(self, head):
        # 32ms 96.97%
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        else:
            return None

        cursor = head
        while cursor is not slow:
            cursor = cursor.next
            slow = slow.next
        return cursor



def main():
    q = Q142()
    q.add_args([3, 2, 0, -4], 1)
    q.run()

if __name__ == '__main__':
    main()
