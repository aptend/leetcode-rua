pub fn increasing_triplet(nums: Vec<i32>) -> bool {
    let mut n1 = std::i32::MAX;
    let mut n2 = std::i32::MAX;
    for &x in &nums {
        if x > n2 {
            return true;
        } else if x > n1 {
            n2 = x;
        } else if x < n1 {
            n1 = x;
        }
    }
    false
}

#[test]
fn test_334() {
    assert_eq!(true, increasing_triplet(vec![1, 2, 3, 4, 5]));
    assert_eq!(true, increasing_triplet(vec![5, 2, 6, 4, 5]));
    assert_eq!(false, increasing_triplet(vec![5, 4, 3, 2, 1]));
}
