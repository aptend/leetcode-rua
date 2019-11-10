from leezy import Solution, solution
import string


class Q017(Solution):
    @solution
    def letterCombinations(self, digits):
        # 16ms 83%
        if digits == '':
            return []
        dial = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        total = []
        self.dfs(dial, digits, 0, '', total)
        return total

    def dfs(self, dial, digits, i, current, total):
        if i == len(digits):
            total.append(current)
            return
        for ch in dial[digits[i]]:
            self.dfs(dial, digits, i+1, current+ch, total)



def main():
    q = Q017()
    q.add_args('23')
    q.run()


if __name__ == "__main__":
    main()
