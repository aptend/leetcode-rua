use std::convert::TryInto;
pub fn integer_break(n: i32) -> i32 {
    if n <= 3 {
        return n - 1;
    }
    let mut n = n as i64;
    let KMOD = 1_000_000_007;
    let mut ans = 1;
    while n > 4 {
        ans = (ans * 3) % KMOD;
        n -= 3;
    }
    ((ans * n) % KMOD).try_into().unwrap()
}

#[test]
fn test_343() {
    assert_eq!(36, integer_break(10));
    assert_eq!(1458, integer_break(20));
    assert_eq!(839082844, integer_break(987));
}
