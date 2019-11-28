pub fn largest_sum_after_k_negations(a: Vec<i32>, k: i32) -> i32 {
    let mut a = a;
    a.sort_unstable();
    for i in 0..k as usize {
        if a[i] < 0 {
            a[i] = -a[i];
        } else if a[i] > 0 {
            if (k - i as i32) % 2 == 0 {
                break;
            }
            if i == 0 {
                a[0] = -a[0];
            } else if a[i - 1].abs() > a[i] {
                a[i] = -a[i];
            } else {
                a[i - 1] = -a[i - 1];
            }
        } else {
            break;
        }
    }
    a.into_iter().sum()
}

#[test]
fn test_1005() {
    assert_eq!(8, largest_sum_after_k_negations(vec![1, 2, 3, 4], 1));
    assert_eq!(6, largest_sum_after_k_negations(vec![3, -1, 0, 2], 3));
    assert_eq!(13, largest_sum_after_k_negations(vec![2, -3, -1, 5, -4], 2));
}
