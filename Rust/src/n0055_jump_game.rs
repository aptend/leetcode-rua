use std::cmp::min;
pub fn can_jump_On2(nums: Vec<i32>) -> bool {
    // 396ms 5%
    let N = nums.len();
    let mut dp = vec![false; N];
    dp[N - 1] = true;
    for i in (0..N - 1).rev() {
        dp[i] = (1..=min(N - 1, i + nums[i] as usize)).rev().any(|x| dp[x]);
    }
    dp[0]
}

pub fn can_jump(nums: Vec<i32>) -> bool {
    // 0ms
    let N = nums.len();
    let mut idx = N - 1;
    for i in (0..N - 1).rev() {
        if i + nums[i] as usize >= idx {
            idx = i;
        }
    }
    idx == 0
}

#[test]
fn test_55() {
    assert_eq!(true, can_jump(vec![2, 3, 1, 1, 4]));
    assert_eq!(false, can_jump(vec![3, 2, 1, 0, 4]));
}
