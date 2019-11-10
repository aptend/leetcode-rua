from leezy import Solution, solution


class Q1185(Solution):
    @solution
    def dayOfTheWeek(self, day, month, year):
        # 36ms 69.10%
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        for i in range(1971, year):
            days += 366 if is_leap(i) else 365
        for i in range(1, month):
            days += month_day[i]
        if month > 2 and is_leap(year):
            days += 1
        days += day
        return week[(days-1) % 7]


def main():
    q = Q1185()
    q.add_args(31, 8, 2019) # Sat
    q.add_args(10, 9, 2019) # Tuesday
    q.run()


if __name__ == "__main__":
    main()
