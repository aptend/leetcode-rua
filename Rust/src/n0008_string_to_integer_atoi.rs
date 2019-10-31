use std::i32::{MAX, MIN};

pub fn my_atoi(str: String) -> i32 {
    let mut tokens = str.trim().chars();
    let mut ans = 0i32;
    let mut flag = 1;
    // handle first char
    if let Some(ch) = tokens.next() {
        if ch == '-' {
            flag = -1;
        } else if ch.is_digit(10) {
            ans = ch.to_digit(10).unwrap() as i32;
        } else if ch != '+' {
            return 0;
        }
    } else {
        return 0;
    }
    // do the left shit
    for ch in tokens {
        if ch.is_digit(10) {
            let d = ch.to_digit(10).unwrap() as i32;
            if ans > MAX / 10 || (ans == MAX / 10 && d > 7) {
                return if flag == 1 { MAX } else { MIN };
            }
            ans = 10 * ans + d;
        } else {
            break;
        }
    }

    flag * ans
}

#[test]
fn test_8() {
    assert_eq!(0, my_atoi("xx".to_owned()));
    assert_eq!(0, my_atoi("".to_owned()));
    assert_eq!(0, my_atoi("+0".to_owned()));
    assert_eq!(0, my_atoi("-0".to_owned()));
    assert_eq!(42, my_atoi("42".to_owned()));
    assert_eq!(42, my_atoi("+42".to_owned()));
    assert_eq!(-42, my_atoi("   -42".to_owned()));
    assert_eq!(0, my_atoi("  - 42".to_owned()));
    assert_eq!(3, my_atoi("0000000000000000003".to_owned()));
    assert_eq!(4396, my_atoi("  +4396 famous  ".to_owned()));
    assert_eq!(2147483647, my_atoi("2147483648".to_owned()));
    assert_eq!(2147483638, my_atoi("2147483638".to_owned()));
    assert_eq!(2147483647, my_atoi("11474836381".to_owned()));
    assert_eq!(-2147483648, my_atoi("-11474836481".to_owned()));
    assert_eq!(-2147483648, my_atoi("-2147483648".to_owned()));
}
