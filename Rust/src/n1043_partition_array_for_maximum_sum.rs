pub fn max_sum_after_partitioning(a: Vec<i32>, k: i32) -> i32 {
    let mut dp = vec![0; a.len() + 1];
    let k = k as usize;
    let mut i = 1;
    for &x in a.iter() {
        let mut max = x;
        for j in 1..=(std::cmp::min(k, i)) {
            max = std::cmp::max(max, a[i - j]);
            dp[i] = std::cmp::max(dp[i], dp[i - j] + j as i32 * max)
        }
        i += 1;
    }
    dp[a.len()]
}

#[test]
fn test_1043() {
    assert_eq!(
        84,
        max_sum_after_partitioning(vec![1, 15, 7, 9, 2, 5, 10], 3)
    );
}
