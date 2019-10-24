from leeyzer import solution, Solution

from collections import defaultdict, deque

class Q1081(Solution):
    @solution
    def smallestSubsequence(self, text):
        # 44ms 27.43%
        # same thought with 
        # https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/308222/show-my-thinking-process
        index_of = defaultdict(deque)
        for i, ch in enumerate(text):
            index_of[ch].append(i)
        ans = []
        cur_index = -1
        for _ in range(len(index_of)):
            keys = sorted(list(index_of.keys()))
            for i, ch in enumerate(keys):
                if all(index_of[ch][0] < index_of[x][-1] for x in keys[i+1:]):
                    cur_index = index_of[ch][0]
                    ans.append(ch)
                    del index_of[ch]
                    break
            for ch in index_of.keys():
                # it is impossible to have a empty list here
                while index_of[ch][0] < cur_index:
                    index_of[ch].popleft()
        return ''.join(ans)
    
    @solution
    def smallest_subseq(self, text):
        # solution from lee215, repsect
        # last occurrence index of each char
        last = {c: i for i, c in enumerate(S)}
        # answer stack
        stack = []
        for i, c in enumerate(S):
            if c in stack: continue
            # if the current character is smaller than the last character in the stack,
            # and the last character exists in the following stream,
            # we can pop the last character to get a smaller result.
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)



def main():
    q = Q1081()
    q.add_args('cdadabcc')
    q.add_args('ecbacba')
    q.run()

if __name__ == '__main__':
    main()
