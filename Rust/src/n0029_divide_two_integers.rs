pub fn divide(dividend: i32, divisor: i32) -> i32 {
    let (mut dd, mut ds) = (dividend, divisor);
    let neg = (dd < 0 && ds > 0) || (dd > 0 && ds < 0);
    let mut ans = 0;
    if ds == std::i32::MIN {
        if dd == std::i32::MIN {
            return 1;
        } else {
            return 0;
        };
    }
    if dd == std::i32::MIN {
        if ds == -1 {
            return std::i32::MAX;
        } else if ds == 1 {
            return dd;
        } else if neg {
            dd += ds;
            ans = 1;
        } else {
            dd -= ds;
            ans = 1;
        }
    }

    dd = dd.abs();
    ds = ds.abs();
    while dd >= ds {
        let mut i = 0;
        while ds << i < std::cmp::min(dd, std::i32::MAX >> 1) {
            i += 1;
        }
        i -= if i > 0 { 1 } else { 0 };
        ans += 1 << i;
        dd -= ds << i;
    }
    if neg {
        -ans
    } else {
        ans
    }
}

#[test]
fn test_29() {
    assert_eq!(3, divide(10, 3));
    assert_eq!(-2, divide(-7, 3));
    assert_eq!(2147483647, divide(-2147483648, -1));
    assert_eq!(-2147483648, divide(-2147483648, 1));
    assert_eq!(1, divide(-2147483648, -2147483648));
    assert_eq!(-1, divide(1100540749, -1090366779));
}
