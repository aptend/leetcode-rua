pub fn num_subarray_bounded_max(a: Vec<i32>, l: i32, r: i32) -> i32 {
    let mut ans = 0;
    let mut dp = 0;
    let mut prev = -1;
    for i in 0..a.len() {
        if a[i] < l {
            ans += dp;
        } else if a[i] > r {
            dp = 0;
            prev = i as i32;
        } else {
            dp = i as i32 - prev;
            ans += dp;
        }
    }
    ans
}

#[test]
fn test_795() {
    assert_eq!(3, num_subarray_bounded_max(vec![2, 1, 4, 3], 2, 3));
}
