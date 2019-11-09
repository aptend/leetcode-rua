pub fn my_sqrt_iter(x: i32) -> i32 {
    if x == 0 || x == 1 {
        x
    } else {
        let mut ans = 2;
        while ans * ans <= x {
            ans += 1;
        }
        ans - 1
    }
}

pub fn my_sqrt(x: i32) -> i32 {
    if x == 0 || x == 1 {
        return x;
    }
    let mut lo = 0;
    let mut hi = x;
    while lo <= hi {
        let mid = lo + (hi - lo) / 2;
        if mid > x / mid {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    lo - 1
}

#[test]
fn test_69() {
    assert_eq!(2, my_sqrt(8));
    assert_eq!(0, my_sqrt(0));
    assert_eq!(1, my_sqrt(1));
    assert_eq!(2, my_sqrt(4));
    assert_eq!(11, my_sqrt(121));
    assert_eq!(46339, my_sqrt(2147395599));
}
