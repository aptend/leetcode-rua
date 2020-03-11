pub fn can_three_parts_equal_sum(a: Vec<i32>) -> bool {
    let s: i32 = a.iter().sum();
    match s % 3 {
        0 => {
            let s = s / 3;
            let mut i = 0;
            let mut acc;
            for _ in 0..2 {
                acc = a[i];
                i += 1;
                while i < a.len() && acc != s {
                    acc += a[i];
                    i += 1;
                }
                if i == a.len() {
                    return false;
                }
            }
            true
        }
        _ => false,
    }
}

#[test]
fn test_1013() {
    assert_eq!(
        true,
        can_three_parts_equal_sum(vec![0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    );
    assert_eq!(
        false,
        can_three_parts_equal_sum(vec![0, 2, 1, -6, 6, -7, 9, -1, 2, 0, 1])
    );
    assert_eq!(
        true,
        can_three_parts_equal_sum(vec![3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
    );
    assert_eq!(false, can_three_parts_equal_sum(vec![1, -1, 1, -1]));
}
