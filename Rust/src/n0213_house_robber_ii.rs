use std::cmp::max;
pub fn rob(nums: Vec<i32>) -> i32 {
    fn _rob(houses: &[i32]) -> i32 {
        let mut dp0 = 0;
        let mut dp1 = 0;
        for x in houses.iter() {
            let tmp = dp1;
            dp1 = max(dp0 + x, dp1);
            dp0 = tmp;
        }
        dp1
    }
    let N = nums.len();
    match N {
        0 => 0,
        1 => nums[0],
        _ => max(_rob(&nums[..N - 1]), _rob(&nums[1..])),
    }
}

#[test]
fn test_213() {
    assert_eq!(3, rob(vec![2, 3, 2]));
    assert_eq!(4, rob(vec![1, 2, 3, 1]));
}
