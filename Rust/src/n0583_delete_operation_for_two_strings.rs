pub fn min_distance(word1: String, word2: String) -> i32 {
    let (m, n) = (word1.len(), word2.len());
    let w1: Vec<_> = word1.chars().collect();
    let w2: Vec<_> = word2.chars().collect();
    let mut dp = vec![vec![0; n + 1]; m + 1];
    for i in 0..=m {
        for j in 0..=n {
            if i == 0 {
                dp[i][j] = j;
            } else if j == 0 {
                dp[i][j] = i;
            } else if w1[i - 1] == w2[j - 1] {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = std::cmp::min(dp[i - 1][j], dp[i][j - 1]) + 1;
            }
        }
    }
    dp[m][n] as i32
}

#[test]
fn test_583() {
    assert_eq!(2, min_distance("eat".to_owned(), "sea".to_owned()));
}
