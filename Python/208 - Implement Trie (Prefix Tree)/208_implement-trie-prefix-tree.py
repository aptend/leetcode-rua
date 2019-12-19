
# Algo 4 version  recursive


class Node:
    def __init__(self):
        self.next = {}
        self.val = None


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def put(self, node, word, idx):
        if node is None:
            node = Node()
        if idx == len(word):
            node.val = True
            return node
        node.next[word[idx]] = self.put(
            node.next.get(word[idx], None), word, idx+1)
        return node

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.put(self.root, word, 0)

    def get(self, node, word, idx):
        if node is None:
            return None
        if idx == len(word):
            return node
        return self.get(node.next.get(word[idx], None), word, idx+1)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.get(self.root, word, 0)
        if node is None or node.val is None:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.get(self.root, prefix, 0)
        return node is not None


# leetcode version  iterative
class TrieA:

    def __init__(self):
        self.children = {}
        self.is_final = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_final = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_final

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


def main():
    trie = Trie()
    operations = ['insert', 'search', 'search',
                  'startsWith', 'insert', 'search']
    oprands = [['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']]
    for opt, opd in zip(operations, oprands):
        if hasattr(trie, opt):
            print(getattr(trie, opt).__call__(*opd))


if __name__ == '__main__':
    main()
