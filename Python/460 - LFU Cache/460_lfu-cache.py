from collections import defaultdict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLinked:
    def __init__(self):
        d_head = Node('^', None)
        d_tail = Node('$', None)
        d_head.next = d_tail
        d_tail.prev = d_head
        self.H = d_head
        self.T = d_tail
        self.cnt = 0

    def append(self, node):
        prev_node = self.T.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.T
        self.T.prev = node
        self.cnt += 1

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
        self.cnt -= 1

    def oldest_node(self):
        return self.H.next

    def __len__(self):
        return self.cnt


class LFUCache:
    # 240 ms, 55.03%
    def __init__(self, capacity):
        self.nodes = {}
        self.freq_chain = defaultdict(DLinked)
        self.cap = capacity
        self.min_freq = 1

    def access_node(self, node):
        chain = self.freq_chain[node.freq]
        chain.delete(node)
        if node.freq == self.min_freq and len(chain) == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_chain[node.freq].append(node)

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            self.access_node(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.access_node(node)
        elif self.cap > 0:
            if len(self.nodes) == self.cap:
                min_chain = self.freq_chain[self.min_freq]
                to_del = min_chain.oldest_node()
                min_chain.delete(to_del)
                del self.nodes[to_del.key]
            node = Node(key, value)
            self.nodes[key] = node
            first_chain = self.freq_chain[1]
            first_chain.append(node)
            self.min_freq = 1


def main():
    lfucache = LFUCache(3)
    # operations = ['put', 'put', 'get', 'put',
    #               'get', 'get', 'put', 'get', 'get', 'get']
    # oprands = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    # [null,null,null,1,null,-1,3,null,-1,3,4]

    operations = ["put", "put", "get", "get", "get", "put", "put",
                  "get", "get", "get", "get"]
    oprands = [[2, 2], [1, 1], [2], [1], [2],
               [3, 3], [4, 4], [3], [2], [1], [4]]
    # None None 2 1 2 None None -1 2 1 4
    for opt, opd in zip(operations, oprands):
        if hasattr(lfucache, opt):
            print(getattr(lfucache, opt).__call__(*opd))


if __name__ == '__main__':
    main()
