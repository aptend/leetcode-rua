from random import randint
from typing import List

class Q384:

    def __init__(self, nums: List[int]):
        self.seed = nums[:]
        self.data = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.data = self.seed[:]
        return self.data

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        N = len(self.data)
        for i in range(N):
            j = randint(i, N-1)
            self.data[i], self.data[j] = self.data[j], self.data[i]
        return self.data

if __name__ == "__main__":
    s = Q384([1, 2, 3])
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())
