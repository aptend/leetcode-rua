from leezy.assists import TreeNode

class FindElements:
    # 216ms without set
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

        # self.seen = set()
        def restore(node, v):
            node.val = v
            if node.left:
                restore(node.left, 2*v+1)
                # self.seen.add(2*v+1)
            if node.right:
                restore(node.right, 2*v+2)
                # self.seen.add(2*v+2)
        restore(self.root, 0)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        # return target in self.seen
        path = []
        while target > 0:
            if target % 2 == 0:
                path.append(0)
                target = (target - 2) / 2
            else:
                path.append(1)
                target = (target - 1) / 2

        def _find(node):
            if not path:
                return True
            d = path.pop()
            if d == 0 and node.right:
                return _find(node.right)
            if d == 1 and node.left:
                return _find(node.left)
            return False

        return _find(self.root)


def main():
    findelements = FindElements(TreeNode.make_tree([-1, None, -1]))
    operations = ['find', 'find']
    oprands = [[1], [2]]
    for opt, opd in zip(operations, oprands):
        if hasattr(findelements, opt):
            print(getattr(findelements, opt).__call__(*opd))


if __name__ == '__main__':
    main()
