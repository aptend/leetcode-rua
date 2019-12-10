from leezy.assists import TreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def ser(node):
            if node is None:
                vals.append('#')
                return
            vals.append(str(node.val))
            ser(node.left)
            ser(node.right)
        ser(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split().__iter__()
        def de(iterv):
            v = next(iterv)
            if v == '#':
                return None
            node = TreeNode(int(v))
            node.left = de(iterv)
            node.right = de(iterv)
            return node
        return de(vals)



def main():
    tree = TreeNode.make_tree([1,2,3,None,None,4,5])
    codec = Codec()
    print(codec.deserialize(codec.serialize(tree)))


if __name__ == '__main__':
    main()
