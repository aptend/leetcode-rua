from leezy import solution, Solution

class Q1233(Solution):
    # a reversed process of 820. short encoding of words
    
    @solution
    def removeSubfolders(self, folder):
        # 236ms 92.15%
        folder = sorted(folder)
        ans = [folder[0]]
        for f in folder[1:]:
            # as we sorted by ascii and length,
            # the only possible parent is ans[-1]
            if not f.startswith(ans[-1] + '/'):
                ans.append(f)
        return ans

    @solution
    def remove(self, folder):
        # 312ms
        pool = set(folder)
        if '/' in pool:
            return ['/']
        ans = []
        for f in folder:
            for i, ch in enumerate(f):
                if ch == '/' and f[:i] in pool:
                    break
            else:
                ans.append(f)
        return ans

    @solution
    def remove_subfolders(self, folder):
        # 1952ms my original thought in the contest
        N = len(folder)
        marked = [True] * N
        folder = sorted(folder, key=lambda x: len(x))
        # folder is only sorted by length, we must do a dual loop
        for i in range(N):
            if marked[i]:
                for j in range(i+1, N):
                    if marked[j]:
                        if folder[j].startswith(folder[i]+'/'):
                            marked[j] = False
        ans = []
        for i in range(N):
            if marked[i]:
                ans.append(folder[i])
        return ans


    

def main():
    q = Q1233()
    q.add_args(['/a', '/a/b', '/c/d', '/c/d/e', '/c/f'])
    q.run()

if __name__ == '__main__':
    main()
