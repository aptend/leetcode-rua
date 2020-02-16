from leezy import solution, Solution
from leezy.assists import TreeContext

from collections import deque

class Q958(Solution):
    @solution
    def isCompleteTree(self, root):
        prev = 0
        q = deque()
        q.append((root, 1))
        while q:
            for _ in range(len(q)):
                node, x = q.popleft()
                if x - prev > 1:
                    return False
                prev = x
                if node.left:
                    q.append((node.left, 2*x))
                if node.right:
                    q.append((node.right, 2*x+1))
        return True

    @solution
    def is_complete_tree(self, root):
        q = deque()
        q.append(root)
        term_flag = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if term_flag and (node.left or node.right):
                    return False
                if node.left:
                    q.append(node.left)
                elif node.right:
                    return False
                if node.right:
                    q.append(node.right)
                else:
                    term_flag = True
        return True




def main():
    q = Q958()
    q.set_context(TreeContext)
    q.add_case(q.case([1, 2, 3, 4, 5, 6]).assert_equal(True))
    q.add_case(q.case([1, 2, 3, 4, 5, None, 7]).assert_equal(False))
    q.run()

if __name__ == '__main__':
    main()
