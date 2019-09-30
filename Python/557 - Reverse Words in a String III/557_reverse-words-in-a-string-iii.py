from leeyzer import Solution, solution


class Q557(Solution):
    @solution
    def reverseWords(self, s):
        # 40ms 74.26%
        return ' '.join([s[::-1] for s in s.split()])


def main():
    q = Q557()
    q.add_args("Let's take LeetCode contest")
    q.run()


if __name__ == "__main__":
    main()
