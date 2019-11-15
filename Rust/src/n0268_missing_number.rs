pub fn missing_number(nums: Vec<i32>) -> i32 {
    let N = nums.len() as i32;
    let sum = N * (N + 1) / 2;
    sum - nums.into_iter().sum::<i32>()
}

#[test]
fn test_268() {
    assert_eq!(8, missing_number(vec![9, 6, 4, 2, 3, 5, 7, 0, 1]));
    assert_eq!(2, missing_number(vec![3, 0, 1]));
}
