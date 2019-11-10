from leezy import Solution, solution
from leezy.assists import TreeContext


class Q700(Solution):
    @solution
    def searchBST(self, root, val):
        # 80ms
        if root is None:
            return
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root
        
    @solution
    def search(self, root, val):
        # 60ms 97.06%
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
        return None
        



def main():
    q = Q700()
    q.set_context(TreeContext)
    q.add_args([4, 2, 7, 1, 3], 2)
    q.run()


if __name__ == "__main__":
    main()
