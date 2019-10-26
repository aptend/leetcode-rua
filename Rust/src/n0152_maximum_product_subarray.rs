use std::cmp::{max, min};

pub fn max_product(nums: Vec<i32>) -> i32 {
    // max positive ends with x
    let mut dp0 = nums[0];
    // min negtivie ends with x
    let mut dp1 = nums[0];
    let mut ans = nums[0];
    for &x in nums.iter().skip(1) {
        if x >= 0 {
            dp0 = max(dp0 * x, x);
            dp1 = min(0, dp1 * x);
        } else {
            let tmp = dp0;
            dp0 = max(0, dp1 * x);
            dp1 = min(x, tmp * x);
        }
        ans = max(ans, dp0);
    }
    ans
}

pub fn max_product_concise(nums: Vec<i32>) -> i32 {
    // max positive ends with x
    let mut dp0 = nums[0];
    // min negtivie ends with x
    let mut dp1 = nums[0];
    let mut ans = nums[0];
    for &x in nums.iter().skip(1) {
        let candid = [x, dp0 * x, dp1 * x];
        dp0 = *candid.iter().max().unwrap();
        dp1 = *candid.iter().min().unwrap();
        ans = max(ans, dp0);
    }
    ans
}

#[test]
fn test_152() {
    assert_eq!(2, max_product(vec![2]));
    assert_eq!(-2, max_product(vec![-2]));
    assert_eq!(8, max_product(vec![-2, 2, 2]));
    assert_eq!(6, max_product(vec![2, 3, -2, 4]));
}
