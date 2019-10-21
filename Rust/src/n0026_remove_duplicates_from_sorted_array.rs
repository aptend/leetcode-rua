pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
    if nums.is_empty() {
        return 0;
    }
    let mut i = 0;
    for j in 1..nums.len() {
        if nums[j] != nums[i] {
            i += 1;
            nums[i] = nums[j];
        }
    }
    (i + 1) as i32
}

#[test]
fn test_26() {
    assert_eq!(0, remove_duplicates(&mut vec![]));
    assert_eq!(2, remove_duplicates(&mut vec![1, 1, 2, 2]));
}
