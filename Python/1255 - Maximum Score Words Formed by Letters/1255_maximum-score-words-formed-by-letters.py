from leezy import solution, Solution

from collections import Counter


class Q1255(Solution):
    @solution
    def maxScoreWords(self, words, letters, score):
        # 48ms 100.00%
        counter = Counter(letters)

        def dfs(start, counter, s):
            self.ans = max(self.ans, s)
            for i in range(start, len(words)):
                c = Counter(words[i])
                for ch in c:
                    if ch not in counter:
                        break
                    elif counter[ch] < c[ch]:
                        break
                else:
                    dfs(i+1, counter - c, s +
                        sum(score[ord(ch) - 97] for ch in words[i]))
        self.ans = 0
        dfs(0, counter, 0)
        return self.ans


def main():
    q = Q1255()
    q.add_args(['dog', 'cat', 'dad', 'good'], ['a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'], [
               1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    q.run()


if __name__ == '__main__':
    main()
