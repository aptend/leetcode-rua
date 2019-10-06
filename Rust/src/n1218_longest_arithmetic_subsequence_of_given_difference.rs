use std::collections::HashMap;
pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
    let mut map: HashMap<i32, i32> = HashMap::new();
    for &x in arr.iter() {
        map.insert(x, map.get(&(x - difference)).unwrap_or(&0) + 1);
    }
    *map.values().max().unwrap()
}

#[test]
fn test_1218() {
    assert_eq!(4, longest_subsequence(vec![1, 5, 7, 8, 5, 3, 4, 2, 1], -2));
    assert_eq!(1, longest_subsequence(vec![1, 3, 5, 7], 1));
}
