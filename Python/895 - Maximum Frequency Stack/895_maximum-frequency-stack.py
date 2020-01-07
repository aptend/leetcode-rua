from heapq import heappop, heappush
from collections import Counter, defaultdict


class FreqStackHeap:
    # 364 ms, faster than 23.09%
    # push & pop log(n)
    def __init__(self):
        self.mono_cnt = 0
        self.heap = []
        self.freq = Counter()

    def push(self, x):
        self.freq[x] += 1
        self.mono_cnt += 1
        heappush(self.heap, (-self.freq[x], -self.mono_cnt, x))

    def pop(self):
        _, _, x = heappop(self.heap)
        self.freq[x] -= 1
        return x


class FreqStack:
    # 348ms
    # O(1)
    def __init__(self):
        self.max_f = 0
        self.freq = Counter()
        self.group = defaultdict(list)

    def push(self, x):
        self.freq[x] += 1
        if self.freq[x] > self.max_f:
            self.max_f += 1
        self.group[self.freq[x]].append(x)

    def pop(self):
        x = self.group[self.max_f].pop()
        self.freq[x] -= 1
        if len(self.group[self.max_f]) == 0:
            self.max_f -= 1
        return x


def main():
    freqstack = FreqStack()
    operations = ['push', 'push', 'push', 'push',
                  'push', 'push', 'pop', 'pop', 'pop', 'pop']
    oprands = [[5], [7], [5], [7], [4], [5], [], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(freqstack, opt):
            print(getattr(freqstack, opt).__call__(*opd))


if __name__ == '__main__':
    main()
