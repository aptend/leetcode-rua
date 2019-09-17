fn find_target_sum_ways_pull(nums: Vec<i32>, s: i32) -> i32 {
    let sum: i32 = nums.iter().sum();
    if sum < s.abs() || (sum + s) % 2 == 1 {
        return 0;
    }

    let target = ((sum + s) / 2) as usize;
    let mut dp = vec![0; target + 1];
    dp[0] = 1;
    for x in nums.iter().map(|&n| n as usize) {
        for t in (x..=target).rev() {
            dp[t] += dp[t - x];
        }
    }
    dp[target]
}

fn find_target_sum_ways_push(nums: Vec<i32>, s: i32) -> i32 {
    let sum: i32 = nums.iter().sum();
    if sum < s.abs() || (sum + s) % 2 == 1 {
        return 0;
    }

    let target = (sum + s) / 2;
    let mut dp = vec![0; (target + 1) as usize];
    dp[0] = 1;
    for x in nums.iter() {
        for t in (0..=(target-x)).rev() {
            dp[(t + x) as usize] += dp[t as usize];
        }
    }
    dp[target as usize]
}
#[test]
fn test_494() {
    assert_eq!(5, find_target_sum_ways_pull(vec![1, 1, 2, 1, 2], -3));
    assert_eq!(1, find_target_sum_ways_pull(vec![1000], -1000));
    assert_eq!(5, find_target_sum_ways_push(vec![1, 1, 2, 1, 2], -3));
    assert_eq!(1, find_target_sum_ways_push(vec![1000], -1000));
}
