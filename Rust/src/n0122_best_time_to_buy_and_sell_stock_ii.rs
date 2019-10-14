pub fn max_profit(prices: Vec<i32>) -> i32 {
    if prices.len() <= 1 {
        return 0;
    }
    let mut ans = 0;
    let mut hold = -prices[0];
    for (i, &x) in prices.iter().enumerate().skip(1) {
        if x < prices[i - 1] {
            ans += prices[i - 1] + hold;
            hold = -x;
        }
    }
    ans += prices.last().unwrap() + hold;
    ans
}

#[test]
fn test_122() {
    assert_eq!(0, max_profit(vec![7, 6, 5, 4, 2, 1]));
    assert_eq!(7, max_profit(vec![7, 1, 5, 3, 6, 4]));
    assert_eq!(4, max_profit(vec![1, 2, 3, 4, 5]));
}
