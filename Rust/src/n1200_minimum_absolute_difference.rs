pub fn minimum_abs_difference(arr: Vec<i32>) -> Vec<Vec<i32>> {
    let mut arr = arr;
    arr.sort();
    let min_diff = arr
        .iter()
        .zip(arr[1..].iter())
        .map(|(&x, &y)| y - x)
        .min()
        .unwrap();
    let mut ans = vec![];
    for (&x, &y) in arr.iter().zip(arr[1..].iter()) {
        if y - x == min_diff {
            ans.push(vec![x, y]);
        }
    }
    ans
}

#[test]
fn test_1200() {
    assert_eq!(
        vec![vec![1, 5]],
        minimum_abs_difference(vec![5, 1, 10, 100, 20])
    )
}
