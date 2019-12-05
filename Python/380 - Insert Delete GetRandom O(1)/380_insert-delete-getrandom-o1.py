import random


class RandomizedSet:

    def __init__(self):
        # 100ms 91.62%
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.v2idx = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.v2idx:
            return False
        self.v2idx[val] = len(self.vals)
        self.vals.append(val)

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.v2idx:
            return False
        idx = self.v2idx[val]
        self.vals[idx], self.vals[-1] = self.vals[-1], self.vals[idx]
        self.v2idx[self.vals[idx]] = idx
        self.vals.pop()
        del self.v2idx[val]

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.vals:
            return self.vals[random.randint(0, len(self.vals)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main():
    randomizedset = RandomizedSet()
    operations = ['insert', 'remove', 'insert',
                  'getRandom', 'remove', 'insert', 'getRandom']
    oprands = [[1], [2], [2], [], [1], [2], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(randomizedset, opt):
            print(getattr(randomizedset, opt).__call__(*opd))


if __name__ == '__main__':
    main()
