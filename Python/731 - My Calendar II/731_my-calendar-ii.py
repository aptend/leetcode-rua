class MyCalendarTwo:
    # 476ms 83.58%

    def __init__(self):
        self.inv = []
        self.dinv = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.dinv:
            if not(start >= e or end <= s):
                return False

        for (s, e) in self.inv:
            if start >= e or end <= s:
                continue
            self.dinv.append((max(s, start), min(e, end)))
        self.inv.append((start, end))
        return True


def main():
    mycalendartwo = MyCalendarTwo()
    operations = ['book', 'book', 'book', 'book', 'book', 'book']
    oprands = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    for opt, opd in zip(operations, oprands):
        if hasattr(mycalendartwo, opt):
            print(getattr(mycalendartwo, opt).__call__(*opd))


if __name__ == '__main__':
    main()
