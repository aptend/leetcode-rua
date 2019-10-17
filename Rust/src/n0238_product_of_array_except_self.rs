pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let N = nums.len();
    let mut ans = vec![1; N];
    for i in 1..N {
        ans[i] = ans[i - 1] * nums[i - 1];
    }

    let mut r_mul = 1;
    for i in (0..N).rev() {
        ans[i] *= r_mul;
        r_mul *= nums[i];
    }
    ans
}

#[test]
fn test_238() {
    assert_eq!(vec![24, 12, 8, 6], product_except_self(vec![1, 2, 3, 4]));
}
