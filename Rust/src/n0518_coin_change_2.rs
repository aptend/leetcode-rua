pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
    let mut dp = vec![0; (amount + 1) as usize];
    dp[0] = 1;
    for &coin in &coins {
        for x in coin..=amount {
            dp[x as usize] += dp[(x - coin) as usize];
        }
    }
    dp[amount as usize]
}

#[test]
fn test_518() {
    assert_eq!(4, change(5, vec![1, 2, 5]));
    assert_eq!(0, change(5, vec![3]));
    assert_eq!(59349132, change(777, vec![1, 2, 5, 10, 20, 50, 100]));
}
