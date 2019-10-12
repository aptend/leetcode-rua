pub fn unique_paths(m: i32, n: i32) -> i32 {
    if m == 0 || n == 0 {
        return 0;
    }
    let M = m as usize;
    let mut dp = vec![0; M + 1];
    dp[1] = 1;
    for _ in 0..n {
        for i in 1..=M {
            dp[i] += dp[i - 1];
        }
    }
    dp[M]
}

#[test]
fn test_62() {
    assert_eq!(3, unique_paths(3, 2));
    assert_eq!(0, unique_paths(5, 0));
    assert_eq!(1, unique_paths(1, 1));
    assert_eq!(28, unique_paths(7, 3));
}
