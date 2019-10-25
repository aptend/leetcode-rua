pub fn max_width_ramp(a: Vec<i32>) -> i32 {
    let bisect = |stack: &[usize], x: i32| -> usize {
        let (mut lo, mut hi) = (0i32, stack.len() as i32 - 1);
        while lo <= hi {
            let mid = lo + (hi - lo) / 2;
            if a[stack[mid as usize]] <= x {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        stack[lo as usize]
    };

    let mut stack = vec![];
    let mut ans = 0;
    for (i, &x) in a.iter().enumerate() {
        if stack.is_empty() || a[*stack.last().unwrap()] > x {
            stack.push(i);
        } else {
            ans = std::cmp::max(ans, i - bisect(&stack, x));
        }
    }
    ans as i32
}

fn max_width_ramp_plus(a: Vec<i32>) -> i32 {
    let mut stack = vec![];
    let mut ans = 0;
    for (i, &x) in a.iter().enumerate() {
        if stack.is_empty() || a[*stack.last().unwrap()] > x {
            stack.push(i);
        }
    }
    for (i, &x) in a.iter().enumerate().rev() {
        while !stack.is_empty() && a[*stack.last().unwrap()] <= x {
            ans = std::cmp::max(ans, i - stack.pop().unwrap());
        }
    }
    ans as i32
}

#[test]
fn test_962() {
    assert_eq!(4, max_width_ramp(vec![6, 0, 8, 2, 1, 5]));
    assert_eq!(7, max_width_ramp(vec![9, 8, 1, 0, 1, 9, 4, 0, 4, 1]));
}
