pub fn advantage_count(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    let N = a.len();
    let mut sorted_a = a;
    sorted_a.sort();
    let mut b_idx: Vec<usize> = (0..N).collect();
    b_idx.sort_by_key(|&i| b[i]);
    let mut ans = vec![-1; N];
    let mut stash = vec![];
    let mut j = 0;
    for &x in &sorted_a {
        let bi = b_idx[j];
        if x > b[bi] {
            j += 1;
            ans[bi] = x;
        } else {
            stash.push(x);
        }
    }
    for i in 0..N {
        if ans[i] == -1 {
            ans[i] = stash.pop().unwrap();
        }
    }
    ans
}

#[test]
fn test_870() {
    assert_eq!(
        vec![2, 11, 7, 15],
        advantage_count(vec![2, 7, 11, 15], vec![1, 10, 4, 11])
    );
    assert_eq!(
        vec![24, 32, 8, 12],
        advantage_count(vec![12, 24, 8, 32], vec![13, 25, 32, 11])
    );
}
