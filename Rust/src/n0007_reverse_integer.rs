pub fn reverse(x: i32) -> i32 {
    let limit = std::i32::MAX / 10;
    let mut x = x;
    let is_neg = x.is_negative();
    x = x.abs();
    let mut r = 0;
    while x > 0 {
        r = 10 * r + x % 10;
        if r > limit && x > 10 {
            return 0;
        }
        x /= 10
    }
    if is_neg {
        -r
    } else {
        r
    }
}

#[test]
fn test_7() {
    assert_eq!(21, reverse(12000));
    assert_eq!(-121, reverse(-121));
    assert_eq!(-2143847412, reverse(-2147483412));
}
