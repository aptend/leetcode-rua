fn dfs(a: &[i32], used: &mut Vec<bool>, cur: &mut Vec<i32>, total: &mut Vec<Vec<i32>>) {
    if cur.len() == a.len() {
        total.push(cur.clone());
        return;
    }
    for i in 0..a.len() {
        if !used[i] {
            used[i] = true;
            cur.push(a[i]);
            dfs(a, used, cur, total);
            cur.pop().unwrap();
            used[i] = false;
        }
    }
}

pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut used = vec![false; nums.len()];
    let mut cur = vec![];
    let mut total = vec![];
    dfs(&nums, &mut used, &mut cur, &mut total);
    total
}

#[test]
fn test_46() {
    assert_eq!(
        vec![
            vec![1, 2, 3],
            vec![1, 3, 2],
            vec![2, 1, 3],
            vec![2, 3, 1],
            vec![3, 1, 2],
            vec![3, 2, 1]
        ],
        permute(vec![1, 2, 3])
    );
}
