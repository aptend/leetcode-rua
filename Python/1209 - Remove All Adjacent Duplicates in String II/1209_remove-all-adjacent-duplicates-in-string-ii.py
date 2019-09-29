from leeyzer import Solution, solution


class Q1209(Solution):
    @solution
    def removeDuplicates(self, s, k):
        # 116ms
        stack = [['', 0]]
        for x in s:
            prev = stack[-1]
            if prev[0] == x:
                if prev[1] == k-1:
                    stack.pop()
                else:
                    prev[1] += 1
            else:
                stack.append([x, 1])
        return ''.join([item[0]*item[1] for item in stack])


def main():
    q = Q1209()
    q.add_args('abcd', 2)
    q.run()


if __name__ == "__main__":
    main()
