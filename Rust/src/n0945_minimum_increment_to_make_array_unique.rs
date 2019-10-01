pub fn min_increment_for_unique(a: Vec<i32>) -> i32 {
    let mut A = a;
    A.sort_unstable();
    let mut n = -1i32;
    let mut ans = 0i32;
    for &x in A.iter() {
        if n < x {
            n = x;
        } else {
            ans += n - x + 1;
            n += 1;
        }
    }
    ans
}

#[test]
fn test_945() {
    assert_eq!(1, min_increment_for_unique(vec![1, 2, 2]));
    assert_eq!(2, min_increment_for_unique(vec![0, 0, 2, 2]));
    assert_eq!(6, min_increment_for_unique(vec![3, 2, 1, 2, 1, 7]));
}
