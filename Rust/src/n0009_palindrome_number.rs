pub fn is_palindrome(x: i32) -> bool {
    if x < 0 {
        return false;
    } else if x < 10 {
        return true;
    } else if x % 10 == 0 {
        return false;
    }

    let mut rx = 0;
    let mut x = x;
    while x > rx {
        rx = 10 * rx + x % 10;
        x = x / 10;
    }
    rx == x || x == rx / 10
}

#[test]
fn test_9() {
    assert_eq!(true, is_palindrome(121));
    assert_eq!(true, is_palindrome(100001));
}
