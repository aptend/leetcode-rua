use std::collections::HashMap;
pub fn longest_arith_seq_length(a: Vec<i32>) -> i32 {
    let mut dp = HashMap::new();
    let mut ans = 0;
    for (i, &x) in a.iter().enumerate() {
        for j in 0..i {
            let delta = x - a[j];
            let candi = *dp.get(&(j, delta)).unwrap_or(&0) + 1;
            if candi > *dp.get(&(i, delta)).unwrap_or(&0) {
                dp.insert((i, delta), candi);
                ans = std::cmp::max(ans, candi);
            }
        }
    }
    ans + 1
}

#[test]
fn test_1027() {
    assert_eq!(longest_arith_seq_length(vec![1]), 1);
    assert_eq!(longest_arith_seq_length(vec![3, 3, 3, 3]), 4);
    assert_eq!(longest_arith_seq_length(vec![3, 6, 9, 12]), 4);
    assert_eq!(longest_arith_seq_length(vec![9, 4, 7, 2, 10]), 3);
    assert_eq!(longest_arith_seq_length(vec![20, 1, 15, 3, 10, 5, 8]), 4);
}
