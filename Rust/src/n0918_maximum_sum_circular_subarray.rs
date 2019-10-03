use std::cmp::{max, min};
pub fn max_subarray_sum_circular(a: Vec<i32>) -> i32 {
    let mut dp0 = 0;
    let mut dp1 = 0;
    let mut max_ = std::i32::MIN;
    let mut min_ = std::i32::MAX;
    for &x in &a {
        dp0 = max(x, dp0 + x);
        max_ = max(max_, dp0);
        dp1 = min(x, dp1 + x);
        min_ = min(min_, dp1);
    }
    let sum: i32 = a.iter().sum();
    if sum == min_ {
        max_
    } else {
        max(max_, sum - min_)
    }
}

#[test]
fn test_918() {
    assert_eq!(3, max_subarray_sum_circular(vec![1, -2, 3, -2]));
    assert_eq!(10, max_subarray_sum_circular(vec![5, -3, 5]));
    assert_eq!(4, max_subarray_sum_circular(vec![3, -1, 2, -1]));
    assert_eq!(3, max_subarray_sum_circular(vec![3, -2, 2, -3]));
    assert_eq!(-1, max_subarray_sum_circular(vec![-2, -3, -1]));
    assert_eq!(15, max_subarray_sum_circular(vec![-2, 4, -5, 4, -5, 9, 4]));
}
