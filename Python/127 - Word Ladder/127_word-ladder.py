from leezy import Solution, solution
from collections import defaultdict, deque


class Q127(Solution):
    @solution
    def ladderLength(self, beginWord, endWord, wordList):
        # 140ms 61.49%
        if endWord not in wordList:
            return 0
        transform = defaultdict(set)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                transform[word[:i]+'*'+word[i+1:]].add(word)
        queue = deque()
        queue.append(beginWord)
        seen = set()
        cnt = 0
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                tile = queue.popleft()
                for i in range(L):
                    candidates = transform[tile[:i]+'*'+tile[i+1:]]
                    if endWord in candidates:
                        return cnt+1
                    queue.extend(candidates - seen)
                    seen |= candidates
        return 0

    @solution
    def ladder_bibfs(self, beginWord, endWord, wordList):
        # 76ms 98.14%
        if endWord not in wordList:
            return 0
        transform = defaultdict(set)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                transform[word[:i]+'*'+word[i+1:]].add(word)

        s1, s2, seen = {beginWord}, {endWord}, set()
        cnt = 0
        while s1 and s2:
            cnt += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            nxt_s = set()
            for tile in s1:
                for i in range(L):
                    candidates = transform[tile[:i]+'*'+tile[i+1:]]
                    if len(candidates) == 0:
                        continue
                    if len(candidates & s2) > 0:
                        return cnt+1
                    nxt_s |= candidates - seen
                    seen |= candidates
            s1 = nxt_s
        return 0


def main():
    q = Q127()
    q.add_args("hit", "cog",
               ["hot", "dot", "dog", "lot", "log", "cog"])  # 5
    q.add_args("hit", "mot",
               ["hie", "dot", "mit", "mot", "dog", "lot", "log", "cog"])  # 3
    q.add_args("hit", "cog",
               ["hot", "dot", "dog", "lot", "log"])  # 0
    q.run()

if __name__ == '__main__':
    main()
