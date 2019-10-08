pub fn nums_same_consec_diff(n: i32, k: i32) -> Vec<i32> {
    if n == 1 {
        return (0..10).collect::<Vec<i32>>();
    }
    let mut dp: Vec<i32> = (1..10).collect();
    let mut new_dp: Vec<i32> = vec![];
    for _ in 0..(n - 1) {
        for x in &dp {
            let r = x % 10;
            if r >= k {
                new_dp.push(x * 10 + r - k);
            }
            if k > 0 && r <= 9 - k {
                new_dp.push(x * 10 + r + k);
            }
        }
        std::mem::swap(&mut dp, &mut new_dp);
        new_dp.clear();
    }
    dp
}

#[test]
fn test_967() {
    assert_eq!(
        vec![11, 22, 33, 44, 55, 66, 77, 88, 99],
        nums_same_consec_diff(2, 0)
    );
    assert_eq!(vec![181, 292, 707, 818, 929], nums_same_consec_diff(3, 7));
    assert_eq!(
        vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        nums_same_consec_diff(1, 5)
    );
}
