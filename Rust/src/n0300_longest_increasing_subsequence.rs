pub fn length_of_lis(nums: Vec<i32>) -> i32 {
    let mut best_seq = vec![];
    for x in &nums {
        let idx = match best_seq.binary_search(x) {
            Ok(i) => i,
            Err(i) => i,
        };
        if idx >= best_seq.len() {
            best_seq.push(*x);
        } else {
            best_seq[idx] = *x;
        }
    }
    best_seq.len() as i32
}

#[test]
fn test_300() {
    assert_eq!(3, length_of_lis(vec![1, 2, 3]));
    assert_eq!(4, length_of_lis(vec![10, 9, 2, 5, 3, 7, 101, 18]));
    assert_eq!(1, length_of_lis(vec![2, 2, 2]));
}
