pub fn num_decodings(s: String) -> i32 {
    let chs: Vec<_> = s.chars().collect();
    let mut dp = vec![0; chs.len() + 1];
    dp[0] = 1;
    for i in 1..=chs.len() {
        dp[i] += if chs[i - 1] != '0' { dp[i - 1] } else { 0 };
        if i >= 2 && chs[i - 2] != '0' && s[(i - 2)..i].parse::<i32>().unwrap() <= 26 {
            dp[i] += dp[i - 2];
        }
    }
    dp[chs.len()]
}

#[test]
fn test_91() {
    assert_eq!(2, num_decodings("17".to_owned()));
    assert_eq!(1, num_decodings("27".to_owned()));
    assert_eq!(4, num_decodings("12712".to_owned()));
    assert_eq!(3, num_decodings("226".to_owned()));
}
