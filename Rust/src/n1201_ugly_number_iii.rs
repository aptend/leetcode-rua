pub fn nth_ugly_number(n: i32, a: i32, b: i32, c: i32) -> i32 {
    fn gcd(mut x: i64, mut y: i64) -> i64 {
        while y > 0 {
            let tmp = x;
            x = y;
            y = tmp % y;
        }
        x
    }

    let (n, a, b, c) = (n as i64, a as i64, b as i64, c as i64);
    let ab = a * b / gcd(a, b);
    let ac = a * c / gcd(a, c);
    let bc = b * c / gcd(b, c);
    let abc = ab * c / gcd(ab, c);

    let small_cnt = |x| x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc;

    let mut lo = 1;
    let mut hi = 2e9 as i32 + 1;
    while lo <= hi {
        let mid = lo + (hi - lo) / 2;
        if small_cnt(mid as i64) >= n {
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
