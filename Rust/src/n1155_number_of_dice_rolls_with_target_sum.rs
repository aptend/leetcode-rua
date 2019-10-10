pub fn num_rolls_to_target(d: i32, f: i32, target: i32) -> i32 {
    let mut dp = vec![0; (target + 1) as usize];
    let mut nxt_dp = dp.clone();
    dp[0] = 1;
    let MOD = 1e9 as i32 + 7;
    for _ in 0..d as usize {
        for x in 1..=f as usize {
            for t in x..=target as usize {
                nxt_dp[t] = (nxt_dp[t] + dp[t - x]) % MOD;
            }
        }
        std::mem::swap(&mut dp, &mut nxt_dp);
        for p in nxt_dp.iter_mut() {
            *p = 0;
        }
    }
    dp[target as usize]
}

#[test]
fn test_1155() {
    assert_eq!(1, num_rolls_to_target(1, 6, 3));
    assert_eq!(6, num_rolls_to_target(2, 6, 7));
    assert_eq!(1, num_rolls_to_target(2, 5, 10));
    assert_eq!(0, num_rolls_to_target(1, 2, 3));
    assert_eq!(222616187, num_rolls_to_target(30, 30, 500))
}
