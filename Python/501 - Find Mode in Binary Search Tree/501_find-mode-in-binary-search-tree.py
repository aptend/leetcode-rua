from leezy import Solution, solution
from leezy.assists import TreeContext

class Q501(Solution):
    @solution
    def findMode(self, root):
        # 52ms 61.99%
        self.ans = []
        self.mode_cnt = -2
        self.max_cnt = -1
        self.cnt = 0
        self.prev = None
        def find_mode_cnt(node):
            if node is None:
                return
            find_mode_cnt(node.left)
            if node.val == self.prev:
                self.cnt += 1
            else:
                self.max_cnt = max(self.max_cnt, self.cnt)
                self.cnt = 1
            self.prev = node.val
            find_mode_cnt(node.right)
        find_mode_cnt(root)
        self.mode_cnt = max(self.max_cnt, self.cnt)
        self.cnt = 0
        self.prev = 0
        def collect(node):
            if node is None:
                return
            collect(node.left)
            if node.val == self.prev:
                self.cnt += 1
            else:
                self.cnt = 1
            if self.cnt == self.mode_cnt:
                self.ans.append(node.val)
            self.prev = node.val
            collect(node.right)
        collect(root)
        return self.ans



def main():
    q = Q501()
    q.set_context(TreeContext)
    q.add_args([])
    q.add_args([1])
    q.add_args([1, None, 2, 2])
    q.add_args([1, 1, 2, 2])
    q.add_args([1, None, 2, 2, 2])
    q.run()


if __name__ == "__main__":
    main()
