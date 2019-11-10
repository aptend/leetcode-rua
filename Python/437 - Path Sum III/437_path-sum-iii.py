from leezy import Solution, solution
from leezy.assists import TreeContext
from collections import defaultdict

class Q437(Solution):
    @solution
    def pathSum(self, root, sum):
        # 1088ms 18.56%
        if root is None:
            return 0
        return (self.path_from_here(root, sum) +
                self.pathSum(root.left, sum) +
                self.pathSum(root.right, sum))

    def path_from_here(self, node, target):
        if node is None:
            return 0
        target -= node.val
        here_count = int(target == 0)
        return (here_count +
                self.path_from_here(node.left, target) +
                self.path_from_here(node.right, target))

    @solution
    def path_sum_iii(self, root, sum):
        # 36ms 94.41%  link to 560 - sbuarray sum equals k
        sum_cnt_map = defaultdict(int)
        sum_cnt_map[0] += 1
        self.ans = 0

        def walk(node, accum):
            if node is None:
                return
            accum += node.val
            self.ans += sum_cnt_map[accum-sum]
            sum_cnt_map[accum] += 1
            walk(node.left, accum)
            walk(node.right, accum)
            sum_cnt_map[accum] -= 1
        walk(root, 0)
        return self.ans



def main():
    q = Q437()
    q.set_context(TreeContext)
    q.add_args([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8)
    q.add_args([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 3)
    q.run()


if __name__ == "__main__":
    main()
