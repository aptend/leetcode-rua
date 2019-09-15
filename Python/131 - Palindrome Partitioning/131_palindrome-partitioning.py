from leeyzer import Solution, solution


class Q131(Solution):
    @solution
    def partition(self, s):
        # 64ms 82.33%
        current, total = [], []
        self.dfs(s, 0, current, total)
        return total
    
    def dfs(self, s, start, current, total):
        if start == len(s):
            total.append(current[:])
            return
        for i in range(start, len(s)):
            if self.is_palindrome(s, start, i):
                current.append(s[start:i+1])
                self.dfs(s, i+1, current, total)
                current.pop()

    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    @solution
    def partition_memo(self, s):
        # 52ms 92.41%
        current, total = [], []
        l = len(s)
        memo = [[False]*l for _ in range(l)]
        for i in range(l-1, -1, -1):
            for j in range(l-1, i-1, -1):
                if i == j:
                    memo[i][j] = True
                elif j == i+1:
                    memo[i][j] = s[i] == s[j]
                else:
                    if memo[i+1][j-1] and s[i] == s[j]:
                        memo[i][j] = True
        self.dfs_memo(s, 0, memo, current, total)
        return total

    def dfs_memo(self, s, start, memo, current, total):
        if start == len(s):
            total.append(current[:])
            return
        for i in range(start, len(s)):
            if memo[start][i]:
                current.append(s[start:i+1])
                self.dfs_memo(s, i+1, memo, current, total)
                current.pop()


def main():
    q = Q131()
    q.add_args('aab')
    q.run()


if __name__ == "__main__":
    main()
