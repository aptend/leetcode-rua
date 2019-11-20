pub fn find_nth_digit(n: i32) -> i32 {
    // g_ means group_
    let mut n = n;
    let mut g_first = 1i32;
    let mut g_unit_len = 1i32;
    // g_unit_len * g_first * 9 = how many digits in current group
    while n > g_unit_len.saturating_mul(g_first * 9) {
        n -= g_unit_len.saturating_mul(g_first * 9);
        g_first *= 10;
        g_unit_len += 1;
    }
    // ith number in current group, jth digit in ith number
    let (i, j) = ((n - 1) / g_unit_len, (n - 1) % g_unit_len);
    let mut ith_num = g_first + i;
    for _ in 0..(g_unit_len - 1 - j) {
        ith_num /= 10;
    }
    ith_num % 10
}

#[test]
fn test_400() {
    assert_eq!(0, find_nth_digit(11));
    assert_eq!(8, find_nth_digit(2886));
    assert_eq!(1, find_nth_digit(1000000000));
}
