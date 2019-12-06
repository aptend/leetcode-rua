from collections import defaultdict
import random


class RandomizedCollection:
    # 108ms 83.73%
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.v2idx = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        found = val in self.v2idx
        self.v2idx[val].add(len(self.vals))
        self.vals.append(val)
        return not found

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.v2idx:
            return False
        idx = self.v2idx[val].pop()
        self.vals[idx], self.vals[-1] = self.vals[-1], self.vals[idx]
        self.v2idx[self.vals[idx]].add(idx)
        self.v2idx[self.vals[idx]].remove(len(self.vals)-1)
        self.vals.pop()
        if len(self.v2idx[val]) == 0:
            del self.v2idx[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self.vals:
            return self.vals[random.randint(0, len(self.vals)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main():
    randomizedcollection = RandomizedCollection()
    operations = ['insert', 'insert',
                  'insert', 'getRandom', 'remove', 'getRandom']
    oprands = [[1], [1], [2], [], [1], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(randomizedcollection, opt):
            print(getattr(randomizedcollection, opt).__call__(*opd))


if __name__ == '__main__':
    main()
