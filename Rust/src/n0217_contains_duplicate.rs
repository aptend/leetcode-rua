pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    let N = nums.len();
    let s: std::collections::HashSet<_> = nums.into_iter().collect();
    s.len() != N
}

#[test]
fn test_217() {
    assert_eq!(false, contains_duplicate(vec![1, 2, 3, 4]));
    assert_eq!(true, contains_duplicate(vec![1, 2, 3, 1]));
}
