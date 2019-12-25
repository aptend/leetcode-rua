from leezy import solution, Solution


class Q1078(Solution):
    @solution
    def findOcurrences(self, text, first, second):
        # 28ms 80.47%
        signal = 2
        ans = []
        for w in text.split():
            if signal == 0:
                ans.append(w)
                signal = 2
            if w == first:
                signal = 1
            elif w == second and signal == 1:
                signal = 0
            else:
                signal = 2
        return ans


def main():
    q = Q1078()
    q.add_case(q.case('alice is a good girl she is a good student', 'a', 'good').assert_equal(['girl', 'student']))
    q.run()

if __name__ == '__main__':
    main()
