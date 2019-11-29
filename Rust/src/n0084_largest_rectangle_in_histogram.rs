pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
    if heights.is_empty() {
        return 0;
    }
    let mut heights = heights;
    // make it pop all bar in stack
    heights.push(-1);
    let mut ans = heights[0];
    let mut stack = vec![0];
    for i in 1..heights.len() {
        while !stack.is_empty() {
            if heights[*stack.last().unwrap()] >= heights[i] {
                let idx = stack.pop().unwrap();
                if let Some(j) = stack.last() {
                    ans = std::cmp::max(ans, heights[idx] * (i - j - 1) as i32);
                } else {
                    ans = std::cmp::max(ans, heights[idx] * i as i32);
                }
            } else {
                break;
            }
        }
        stack.push(i);
    }
    ans
}

#[test]
fn test_84() {
    assert_eq!(1, largest_rectangle_area(vec![1]));
    assert_eq!(3, largest_rectangle_area(vec![2, 1, 2]));
    assert_eq!(10, largest_rectangle_area(vec![2, 1, 5, 6, 2, 3]));
    assert_eq!(20, largest_rectangle_area(vec![3, 6, 5, 7, 4, 8, 1, 0]));
    assert_eq!(33, largest_rectangle_area(vec![2, 7, 1, 8, 8, 3, 11, 12, 13, 3]));
}
