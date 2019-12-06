class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:
    # 192ms 99.25%

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.map = {}
        self.head = Node('^', None)
        self.tail = Node('$', None)
        self.head.right = self.tail
        self.tail.left = self.head

    def append(self, node):
        self.tail.left.right = node
        node.left = self.tail.left
        node.right = self.tail
        self.tail.left = node
    
    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.map and len(self.map) == self.cap:
            node = self.head.right
            del self.map[node.key]
            self.remove(node)
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.append(node)
        else:
            node = Node(key, value)
            self.append(node)
            self.map[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    lrucache = LRUCache(2)
    operations = ['put', 'put', 'get', 'put',
                  'get', 'put', 'get', 'get', 'get']
    oprands = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    # output = [ None, None, 1, None, -1, None, -1, 3, 4 ]
    for opt, opd in zip(operations, oprands):
        if hasattr(lrucache, opt):
            print(getattr(lrucache, opt).__call__(*opd))


if __name__ == '__main__':
    main()
