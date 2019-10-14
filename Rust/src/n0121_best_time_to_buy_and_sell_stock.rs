pub fn max_profit(prices: Vec<i32>) -> i32 {
    let mut min = std::i32::MAX;
    let mut ans = 0;
    for &x in &prices {
        min = std::cmp::min(min, x);
        ans = std::cmp::max(ans, x - min);
    }
    ans
}

#[test]
fn test_121() {
    assert_eq!(0, max_profit(vec![7, 6, 5, 4, 2, 1]));
    assert_eq!(5, max_profit(vec![7, 1, 5, 3, 6, 4]));
}
