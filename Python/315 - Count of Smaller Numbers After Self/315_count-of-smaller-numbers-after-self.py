from leezy import Solution, solution


class Q315(Solution):
    @solution
    def countSmaller(self, nums):
        """
        和顺序相关的题，所以主动联系排序类算法。

        现在全部乱序无从下手，那么部分有序怎么样？

        归并排序就是从部分有序走向全部有序，所以在构建过程中是否可以数出这样的逆序对呢？

        似乎是可行的。注意到最后的输出，看来是对索引进行排序
        """
        idx = list(range(len(nums)))
        aux = idx[:]
        results = [0] * len(nums)

        def count_smaller(lo, hi):
            if lo >= hi:
                return
            mid = (lo + hi) // 2
            count_smaller(lo, mid)    # 递归保证[lo, mid]有序
            count_smaller(mid+1, hi)  # 递归保证[mid+1, hi]有序
            aux[lo: hi+1] = idx[lo: hi+1]
            i, j = mid, hi
            for k in range(hi, lo-1, -1):  # 从高到低填充位置
                if j <= mid:
                    idx[k] = aux[i]
                    i -= 1
                elif i < lo:
                    idx[k] = aux[j]
                    j -= 1
                elif nums[aux[i]] > nums[aux[j]]:  # 发现逆序对
                    results[aux[i]] += j - mid
                    idx[k] = aux[i]
                    i -= 1
                else:
                    idx[k] = aux[j]
                    j -= 1

        count_smaller(0, len(nums)-1)
        return results

    @solution
    def count_iter(self, nums):
        length = len(nums)
        idx = list(range(length))
        aux = idx[:]
        result = [0] * length
        gap = 1
        while gap < length:
            left_start = 0
            while left_start < length:
                left_end = min(left_start+gap-1, length-1)
                # 不取最小值，允许right_start>right_end，表明right为空
                right_start = left_end + 1
                right_end = min(left_start+gap*2-1, length-1)
                # begin merge
                i, j = left_end, right_end
                for k in range(right_end, left_start-1, -1):
                    if j < right_start:
                        aux[k] = idx[i]
                        i -= 1
                    elif i < left_start:
                        aux[k] = idx[j]
                        j -= 1
                    elif nums[idx[i]] > nums[idx[j]]:
                        result[idx[i]] += j - right_start + 1
                        aux[k] = idx[i]
                        i -= 1
                    else:
                        aux[k] = idx[j]
                        j -= 1
                # end merge
                left_start += gap * 2
            idx, aux = aux, idx
            gap *= 2
        return result


def main():
    q = Q315()
    q.add_args([])
    q.add_args([1, 1])
    q.add_args([5, 2, 6, 1])
    q.add_args([5, 4, 3, 2, 1])
    q.run()


if __name__ == "__main__":
    main()
