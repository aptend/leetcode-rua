pub fn num_squares(n: i32) -> i32 {
    let mut dp: Vec<i32> = (0..=n).collect();
    for i in 1..=n as usize {
        let mut j = 0;
        while j * j <= i {
            dp[i] = std::cmp::min(dp[i], dp[i - j * j] + 1);
            j += 1;
        }
    }
    dp[n as usize]
}

#[test]
fn test_279() {
    assert_eq!(3, num_squares(12));
    assert_eq!(2, num_squares(13));
}
