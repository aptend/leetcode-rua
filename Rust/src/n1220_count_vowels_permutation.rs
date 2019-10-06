#[allow(clippy::many_single_char_names)]
pub fn count_vowel_permutation(n: i32) -> i32 {
    let (a, e, i, o, u) = (0, 1, 2, 3, 4);
    let mut dp = vec![1; 5];
    let mut new_dp = vec![0; 5];
    let MOD = 1e9 as i32 + 7;
    for _ in 0..(n - 1) {
        new_dp[a] = ((dp[e] + dp[u]) % MOD + dp[i]) % MOD;
        new_dp[e] = (dp[a] + dp[i]) % MOD;
        new_dp[i] = (dp[e] + dp[o]) % MOD;
        new_dp[o] = dp[i] % MOD;
        new_dp[u] = (dp[i] + dp[o]) % MOD;
        std::mem::swap(&mut new_dp, &mut dp);
    }
    let mut ans = 0;
    for x in dp.iter() {
        ans = (ans + x) % MOD;
    }
    ans
}

#[test]
fn test_1220() {
    assert_eq!(18208803, count_vowel_permutation(144));
}
