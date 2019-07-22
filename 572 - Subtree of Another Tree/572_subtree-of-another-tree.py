from leeyzer import Solution, solution
from leeyzer.assists import TreeContext

class Q572(Solution):
    @solution
    def isSubtree(self, s, t):
        # 296ms 30.04%
        if s is None:
            return t is None
        if t is None:
            return False
        if self.is_same(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        

    def is_same(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return (s.val == t.val and 
                self.is_same(s.left, t.left) and
                self.is_same(s.right, t.right))
def main():
    q = Q572()
    q.set_context(TreeContext)
    q.add_args([3, 4, 5, 1, 2], [4, 1, 2])
    q.add_args([3, 4, 5, 1, 2, None, None, 0], [4, 1, 2])
    q.run()


if __name__ == "__main__":
    main()
