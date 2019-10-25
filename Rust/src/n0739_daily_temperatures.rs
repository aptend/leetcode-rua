pub fn daily_temperatures(t: Vec<i32>) -> Vec<i32> {
    let mut stack = vec![0];
    let mut ans = vec![0; t.len()];
    for (i, &x) in t.iter().enumerate().skip(1) {
        // given x, we pop all t smaller than x
        // stack is mono decreasing
        while !stack.is_empty() && t[*stack.last().unwrap()] < x {
            let pi = stack.pop().unwrap();
            ans[pi] = (i - pi) as i32;
        }
        stack.push(i)
    }
    ans
}

#[test]
fn test_739() {
    assert_eq!(vec![0], daily_temperatures(vec![42]));
    assert_eq!(
        vec![1, 1, 4, 2, 1, 1, 0, 0],
        daily_temperatures(vec![73, 74, 75, 71, 69, 72, 76, 73])
    );
}
