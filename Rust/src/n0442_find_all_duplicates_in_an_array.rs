pub fn find_duplicates(nums: Vec<i32>) -> Vec<i32> {
    let mut nums = nums;
    let mut ans = vec![];
    for i in 0..nums.len() {
        while nums[i] != nums[(nums[i] - 1) as usize] {
            let j = (nums[i] - 1) as usize;
            nums.swap(i, j);
        }
    }
    for i in 0..nums.len() {
        if nums[i] != (i + 1) as i32 {
            ans.push(nums[i])
        }
    }
    ans
}

#[test]
fn test_442() {
    assert_eq!(vec![3, 2], find_duplicates(vec![4, 3, 2, 7, 8, 2, 3, 1]));
}
