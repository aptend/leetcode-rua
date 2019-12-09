pub fn ship_within_days(weights: Vec<i32>, d: i32) -> i32 {
    let mut lo: i32 = *weights.iter().max().unwrap();
    let mut hi: i32 = weights.iter().sum();
    let days_with_cap = |cap| {
        let mut cnt = 0;
        let mut weight = 0;
        for &w in &weights {
            weight += w;
            if weight > cap {
                weight = w;
                cnt += 1;
            }
        }
        cnt + 1
    };
    while lo <= hi {
        let mid = (lo + hi) / 2;
        if days_with_cap(mid) <= d {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    lo
}

#[test]
fn test_1011() {
    assert_eq!(15, ship_within_days(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5));
    assert_eq!(6, ship_within_days(vec![3, 2, 2, 4, 1, 4], 3));
    assert_eq!(3, ship_within_days(vec![1, 2, 3, 1, 1], 4));
}
