from leeyzer import Solution, solution


class Q763(Solution):
    @solution
    def partitionLabels(self, S):
        segments = {}
        for i, c in enumerate(S):
            if c not in segments:
                segments[c] = [i, i]
            else:
                segments[c][1] = i
        opens = set(v[0] for v in segments.values())
        closes = set(v[1] for v in segments.values())
        on_scanning = 0
        boundary = [-1]
        for i in range(len(S)):
            if i in opens:
                on_scanning += 1
            if i in closes:
                on_scanning -= 1
            if on_scanning == 0:
                boundary.append(i)
        res = []
        for i in range(1, len(boundary)):
            res.append(boundary[i]-boundary[i-1])
        return res

    @solution
    def labels(self, S):
        start = end = 0
        res = []
        for i, c in enumerate(S):
            end = max(end, S.rfind(c))
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res




def main():
    q = Q763()
    q.add_args('')
    q.add_args('ab')
    q.add_args('abaccda')
    q.add_args('ababcbacadefegdehijhklij')
    q.run()


if __name__ == "__main__":
    main()
