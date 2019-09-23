pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
    fn gcd(mut x: i64, mut y: i64) -> i64 {
        while y > 0 {
            let tmp = x;
            x = y;
            y = tmp % y;
        }
        x
    }

    let (n, a, b, c) = (i64::from(n), i64::from(a), i64::from(b), i64::from(c));
    let ab = a * b / gcd(a, b);
    let ac = a * c / gcd(a, c);
    let bc = b * c / gcd(b, c);
    let abc = ab * c / gcd(ab, c);

    let small_cnt = |x| x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;

    let mut lo = 1;
    let mut hi = 2e9 as i32 + 1;
    while lo <= hi {
        let mid = lo + (hi - lo) / 2;
        if small_cnt(i64::from(mid)) >= n {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    lo
}

#[test]
fn test_1201() {
    assert_eq!(4, nth_ugly_number(3, 2, 3, 5));
    assert_eq!(9, nth_ugly_number(3, 3, 3, 3));
    assert_eq!(
        1999999984,
        nth_ugly_number(1000000000, 2, 217983653, 336916467)
    );
}
