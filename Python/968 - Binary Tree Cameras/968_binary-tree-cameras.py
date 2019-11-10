from leezy import Solution, solution
from leezy.assists import TreeContext


class Q968(Solution):
    @solution
    def minCameraCover(self, root):
        # 40ms 28%
        def cover(node):
            if node is None:
                # one-node tree: 1, no-way, 0 -> no-way, 0, x
                # two-node tree: 1, 1, no-way -> no-way, 0, 0
                return 1000, 0, 0
            # 1: all are covered, root has a camera
            # 2: all are covered, root has no camera
            # 3: root only is not covered, root no camera
            l1, l2, l3 = cover(node.left)
            r1, r2, r3 = cover(node.right)
            l_min_cover = min(l1, l2)
            r_min_cover = min(r1, r2)
            h1 = 1 + min(l1, l2, l3) + min(r1, r2, r3)
            h2 = min(l1 + r_min_cover, r1 + l_min_cover)
            h3 = l2 + r2
            return h1, h2, h3
        return min(cover(root)[:2])

def main():
    q = Q968()
    q.set_context(TreeContext)
    q.add_args([0, 0, None, 0, 0])
    q.add_args([0, 0, None, 0, None, 0, None, None, 0])
    q.add_args([0, None, 0, 0, 0, None, None, None, 0])
    q.run()


if __name__ == "__main__":
    main()
