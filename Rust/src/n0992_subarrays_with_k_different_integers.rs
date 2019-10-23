fn at_most(a: &[i32], k: i32) -> i32 {
    let mut count = std::collections::HashMap::new();
    let mut distinct = 0;
    let mut ans = 0;
    let mut i = 0;
    for (j, x) in a.iter().enumerate() {
        *count.entry(*x).or_insert(0) += 1;
        if count[x] == 1 {
            distinct += 1;
        }
        while distinct > k {
            count.entry(a[i]).and_modify(|e| *e -= 1);
            if count[&a[i]] == 0 {
                distinct -= 1;
            }
            i += 1;
        }
        ans += j + 1 - i;
    }
    ans as i32
}

pub fn subarrays_with_k_distinct(a: Vec<i32>, k: i32) -> i32 {
    at_most(&a, k) - at_most(&a, k - 1)
}

#[test]
fn test_992() {
    assert_eq!(7, subarrays_with_k_distinct(vec![1, 2, 1, 2, 3], 2));
    assert_eq!(3, subarrays_with_k_distinct(vec![1, 2, 1, 3, 4], 3));
}
