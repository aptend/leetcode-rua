from leeyzer import Solution, solution
from collections import defaultdict

class UF:
    def __init__(self, size=0):
        self.parents = list(range(size))
        self.ranks = [0] * size
        self.count = size

    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

    def insert_slot(self):
        self.parents.append(len(self.parents))
        self.ranks.append(0)
        self.count += 1

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return
        if self.ranks[rp] > self.ranks[rq]:
            self.parents[rq] = rp
        elif self.ranks[rp] < self.ranks[rq]:
            self.parents[rp] = rq
        else:
            self.parents[rq] = rp
            self.ranks[rp] += 1
        self.count -= 1


class Q721(Solution):
    @solution
    def accountsMerge(self, accounts):
        # 368ms 15.59%
        acc = {}
        for entry in accounts:
            name = entry[0]
            emails = set(entry[1:])
            if name not in acc:
                acc[name] = [emails]
            else:
                new_list = []
                for s in acc[name]:
                    if len(emails & s) > 0:
                        emails |= s
                    else:
                        new_list.append(s)
                new_list.append(emails)
                acc[name] = new_list
        ans = []
        for name, email_list in acc.items():
            for e_set in email_list:
                entry = [name]
                entry.extend(sorted(e_set))
                ans.append(entry)
        return ans
    
    @solution
    def acc_merge(self, accounts):
        # 232ms 40.00%
        uf = UF(0)
        e2id = {}
        id2name = []
        idx = 0
        for entry in accounts:
            name = entry[0]
            for email in entry[1:]:
                if email not in e2id:
                    uf.insert_slot()
                    e2id[email] = idx
                    idx += 1
                    id2name.append(name)
                uf.union(e2id[entry[1]], e2id[email])
        res = defaultdict(list)
        for email, id_ in e2id.items():
            res[uf.find(id_)].append(email)

        ans = []
        for root_id, emails_list in res.items():
            entry = [id2name[root_id]]
            entry.extend(sorted(emails_list))
            ans.append(entry)
        return ans


def main():
    q = Q721()
    q.add_args([['John', 'johnsmith@mail.com', 'john_newyork@mail.com'],
                ['John', 'johnsmith@mail.com', 'john00@mail.com'],
                ['Mary', 'mary@mail.com'],
                ['John', 'johnnybravo@mail.com']])
    q.run()


if __name__ == "__main__":
    main()
