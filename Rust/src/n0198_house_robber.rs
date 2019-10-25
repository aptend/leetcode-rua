pub fn rob(nums: Vec<i32>) -> i32 {
    let mut dp0 = 0;
    let mut dp1 = 0;
    for x in &nums {
        let tmp = std::cmp::max(dp0, dp1);
        dp1 = dp0 + x;
        dp0 = tmp;
    }
    std::cmp::max(dp0, dp1)
}

#[test]
fn test_198() {
    assert_eq!(4, rob(vec![1, 2, 3, 1]));
    assert_eq!(12, rob(vec![2, 7, 9, 3, 1]));
}
