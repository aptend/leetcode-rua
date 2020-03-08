pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
    let amount = amount as usize;
    let MAX = std::i32::MAX / 2 + 1;
    let mut dp = vec![MAX; amount + 1];
    dp[0] = 0;
    for &x in &coins {
        let x = x as usize;
        if x > amount {
            continue;
        }
        for j in 0..=(amount - x) {
            dp[j + x] = std::cmp::min(dp[j + x], dp[j] + 1);
        }
    }
    if dp[amount] >= MAX {
        -1
    } else {
        dp[amount]
    }
}

#[test]
fn test_322() {
    assert_eq!(0, coin_change(vec![1, 2, 5], 0));
    assert_eq!(3, coin_change(vec![1, 2, 5], 11));
    assert_eq!(-1, coin_change(vec![2], 11));
}
