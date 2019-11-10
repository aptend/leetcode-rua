from leezy import Solution, solution

from collections import defaultdict, Counter

class Q1156(Solution):
    @solution
    def maxRepOpt1(self, text):
        # 68ms 87.53%
        N = len(text)
        table = defaultdict(list)
        # [start, end, length]
        # 'aaabbcbbbabbbbb' ->
        # { 'a': [[0, 2, 3], [9, 9, 1]],
        #   'b': [[3, 4, 2], [6, 8, 3], [10, 14, 5]],
        #   'c': [[5, 5, 1]]
        # }
        i = j = 0
        for j in range(N-1):
            if text[j] != text[j+1]:
                table[text[i]].append([i, j, j-i+1])
                i = j + 1
        table[text[i]].append([i, N-1, N-i])

        ans = 0
        for group in table.values():
            n = len(group)
            if n <= 1:
                ans = max(ans, group[0][2])
                continue
            delta = 1 if n > 2 else 0
            for i in range(n-1):
                if group[i+1][0] - group[i][1] == 2:
                    # if n > 2, we can always borrow a char from another group
                    candidate = group[i+1][2] + group[i][2] + delta
                    ans = max(ans, candidate)
                else:
                    # we can't connect with other group, 
                    # but we can borrow a char to extend current group
                    ans = max(ans, group[i][2] + 1)
            ans = max(ans, group[n-1][2] + 1)
        return ans
    
    @solution
    def max_repeated(self, text):
        # 68ms
        # solution inspired by 424 longest repeating character replacement
        counter = Counter(text)
        win_cnt = defaultdict(int)
        N = len(text)
        max_freq = 0
        max_char = ''
        i = j = 0
        ans = 0
        for j in range(N):
            ch = text[j]
            win_cnt[ch] += 1
            if win_cnt[ch] > max_freq:
                max_freq = win_cnt[ch]
                max_char = ch
            if j - i + 1 - max_freq > 1:
                # if there is max_char outside of the window, we can borrow it
                if counter[max_char] > max_freq:
                    ans = max(ans, j - i)
                else:
                    ans = max(ans, max_freq)
                win_cnt[text[i]] -= 1
                i += 1
        
        if counter[max_char] > max_freq:
            ans = max(ans, N - i)
        else:
            ans = max(ans, max_freq)
        return ans


def main():
    q = Q1156()
    q.add_args('babbaaabbbbbaa')
    q.add_args('ababa')
    q.add_args('aaabaaa')
    q.add_args('aaabbaaa')
    q.add_args('aaaaa')
    q.add_args('abcdef')
    q.add_args('aaabbcbbbabbbbb')
    q.run()


if __name__ == "__main__":
    main()
