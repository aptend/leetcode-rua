pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
    let mut houses = vec![0; 100_001];
    for &x in &nums {
        houses[x as usize] += x;
    }
    // let's rob
    let mut dp0 = 0;
    let mut dp1 = 0;
    for &h in &houses {
        let tmp = dp1;
        dp1 = h + dp0;
        dp0 = std::cmp::max(tmp, dp0);
    }
    std::cmp::max(dp0, dp1)
}

#[test]
fn test_740() {
    assert_eq!(9, delete_and_earn(vec![2, 2, 3, 3, 3, 4]));
    assert_eq!(6, delete_and_earn(vec![3, 4, 2]));
}
