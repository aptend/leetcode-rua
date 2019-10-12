pub fn max_area(height: Vec<i32>) -> i32 {
    let (mut i, mut j) = (0, height.len() - 1);
    let mut ans = 0;
    while i < j {
        let h = std::cmp::min(height[i], height[j]);
        ans = std::cmp::max(ans, h * (j - i) as i32);
        if h == height[i] {
            i += 1;
        } else {
            j -= 1;
        }
    }
    ans
}

#[test]
fn test_11() {
    assert_eq!(1, max_area(vec![1, 1]));
    assert_eq!(49, max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]));
}
