use std::cmp::max;
pub fn k_concatenation_max_sum(arr: Vec<i32>, k: i32) -> i32 {
    let mut g_max = 0i32;
    let mut dp = 0;
    for &x in arr.iter() {
        dp = max(x, dp + x);
        g_max = max(g_max, dp);
    }
    let max_ee = dp;
    dp = 0;
    for &x in arr.iter().rev() {
        dp = max(x, dp + x);
    }
    let max_ss = dp;

    let sum = max(arr.iter().sum(), 0);
    g_max = max(g_max, sum);

    if k >= 2 {
        let MOD = 10i32.pow(9) + 7;
        let mut concat_sum = max_ss + max_ee;
        for _ in 2..k {
            concat_sum = (concat_sum + sum) % MOD;
        }
        g_max = max(g_max, concat_sum);
    }
    g_max
}


#[test]
fn test_1191() {
    assert_eq!(9, k_concatenation_max_sum(vec![1, 2], 3));
    assert_eq!(0, k_concatenation_max_sum(vec![-1, -2], 3));
    assert_eq!(20, k_concatenation_max_sum(vec![-2, -5, 0, 0, 3, 9, -5, -2, 4], 5));
}
