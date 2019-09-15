from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q100(Solution):
    @solution
    def isSameTree(self, p, q):
        # 20ms
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    @solution
    def is_same_iter(self, p, q):
        # 16ms 81.04%
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            p = stack_p.pop()
            q = stack_q.pop()
            if p is None and q is None:
                continue
            if p and q and p.val == q.val:
                stack_p.append(p.left)
                stack_p.append(p.right)
                stack_q.append(q.left)
                stack_q.append(q.right)
            else:
                return False
        return True

def main():
    q = Q100()
    q.set_context(TreeContext)
    q.add_args([1, 2, 3], [1, 2, 3])
    q.add_args([1, 2, 1], [1, 1, 2])
    q.add_args([1, 2], [1, None, 2])
    q.run()


if __name__ == "__main__":
    main()
