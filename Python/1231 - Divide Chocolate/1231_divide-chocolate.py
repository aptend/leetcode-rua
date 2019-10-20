from leeyzer import solution, Solution

class Q1231(Solution):
    @solution
    def maximizeSweetness(self, sweetness, K):
        # similar problems
        # 1231. Divide Chocolate
        # 1101. Capacity To Ship Packages In N Days
        # 875. Koko Eating Bananas
        # 774. Minimize Max Distance to Gas Station
        # 410. Split Array Largest Sum
        def divide(min_s):
            # when minimum sweetness is set as min_s
            # how many parts we can get at most?
            cuts = part_s = 0
            for s in sweetness:
                part_s += s
                if part_s >= min_s:
                    cuts += 1
                    part_s = 0
            return cuts
        
        lo, hi = 0, sum(sweetness) // (K+1)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if divide(mid) > K:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

def main():
    q = Q1231()
    q.add_args([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    q.add_args([5, 6, 7, 8, 9, 1, 2, 3, 4], 8)
    q.add_args([1, 2, 2, 1, 2, 2, 1, 2, 2], 2)
    q.run()

if __name__ == '__main__':
    main()
