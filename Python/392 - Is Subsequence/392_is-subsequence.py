from leezy import Solution, solution
from collections import defaultdict
from bisect import bisect_left

class Q392(Solution):
    @solution
    def isSubsequence(self, s, t):
        # 88ms 81.20%
        if s == '':
            return True
        if t == '':
            return False
        i = 0
        len_s = len(s)
        for x in t:
            if x == s[i]:
                i += 1
                if i == len_s:
                    return True
        return False

    @solution
    def is_subsequence(self, s, t):
        # 44ms
        iter_t = iter(t)
        return all(ch in iter_t for ch in s)

    @solution
    def is_subsequence_binary_search(self, s, t):
        idx_map = defaultdict(list)
        for idx, ch in enumerate(t):
            idx_map[ch].append(idx)
        
        threshold = 0
        for ch in s:
            array = idx_map[ch]
            # find ch's next postion in S,
            # where it's index should be greater than the index we've inspected
            idx = bisect_left(array, threshold)
            if idx == len(array):
                return False
            threshold = array[idx] + 1
        return True





def main():
    q = Q392()
    q.add_args('', '')
    q.add_args('', 'ahbgdc')
    q.add_args('ab', 'ab')
    q.add_args('abc', 'ahbgdc')
    q.add_args('axc', 'ahbgdc')
    q.run()


if __name__ == "__main__":
    main()
