use std::collections::HashMap;

pub fn subarray_sum(A: Vec<i32>, k: i32) -> i32 {
    let mut map: HashMap<i32, i32> = HashMap::new();
    let mut accum = 0;
    let mut ans = 0;
    map.insert(0, 1);
    for x in A.iter() {
        accum += x;
        ans += map.get(&(accum - k)).unwrap_or(&0);
        *map.entry(accum).or_insert(0) += 1;
    }
    ans
}

#[test]
fn test_560() {
    assert_eq!(2, subarray_sum(vec![1, 1, 1], 2));
    assert_eq!(5, subarray_sum(vec![1, 1, -1, 1], 1));
}
