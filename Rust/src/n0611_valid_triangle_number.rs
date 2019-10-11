pub fn triangle_number(nums: Vec<i32>) -> i32 {
    let mut ans = 0;
    let mut nums = nums;
    nums.sort_unstable();
    for (k, x) in nums.iter().enumerate().skip(2) {
        let (mut i, mut j) = (0, k - 1);
        while i < j {
            let sum = nums[i] + nums[j];
            if sum > *x {
                ans += (j - i) as i32;
                j -= 1;
            } else {
                i += 1;
            }
        }
    }
    ans
}

#[test]
fn test_611() {
    assert_eq!(0, triangle_number(vec![2, 2]));
    assert_eq!(3, triangle_number(vec![2, 2, 3, 4]));
    assert_eq!(9, triangle_number(vec![2, 2, 3, 4, 45, 4, 12, 7]));
}
