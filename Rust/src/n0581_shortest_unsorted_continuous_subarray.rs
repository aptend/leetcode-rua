pub fn find_unsorted_subarray_origin_thought(nums: Vec<i32>) -> i32 {
    let mut ground = vec![0; nums.len()];
    let mut max = std::i32::MIN;
    for (i, n) in nums.iter().enumerate() {
        max = std::cmp::max(max, *n);
        ground[i] = max;
    }
    let mut right = 0;
    for i in (0..nums.len()).rev() {
        if nums[i] < ground[i] {
            right = i;
            break;
        }
    }
    if right == 0 {
        return 0;
    }

    let mut min = std::i32::MAX;
    for (i, n) in nums.iter().enumerate().rev() {
        min = std::cmp::min(min, *n);
        ground[i] = min;
    }
    let mut left = 0;
    for i in 0..nums.len() {
        if nums[i] > ground[i] {
            left = i;
            break;
        }
    }

    (right - left + 1) as i32
}

pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
    // O(1) space
    let mut right = 0;
    let mut max = std::i32::MIN;
    for (i, n) in nums.iter().enumerate() {
        max = std::cmp::max(max, *n);
        if nums[i] < max {
            right = i;
        }
    }
    if right == 0 {
        return 0;
    }

    let mut left = 0;
    let mut min = std::i32::MAX;
    for (i, n) in nums.iter().enumerate().rev() {
        min = std::cmp::min(min, *n);
        if nums[i] > min {
            left = i;
        }
    }

    (right - left + 1) as i32
}

#[test]
fn test_581() {
    assert_eq!(0, find_unsorted_subarray(vec![1, 2, 3]));
    assert_eq!(3, find_unsorted_subarray(vec![3, 2, 1]));
    assert_eq!(3, find_unsorted_subarray(vec![1, 5, 3, 4, 15]));
    assert_eq!(4, find_unsorted_subarray(vec![4, 5, 3, 4, 15]));
}
