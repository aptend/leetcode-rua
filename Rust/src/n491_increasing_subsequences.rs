
use std::collections::HashSet;
use std::i32::MIN;

fn dfs(nums: &Vec<i32>, s: usize, cur: &mut Vec<i32>, total: &mut Vec<Vec<i32>>){
    if cur.len() >= 3 {
        total.push(cur[1..].to_owned());
    }

    let mut used: HashSet<i32> = HashSet::new();
    for i in s..nums.len() {
        if !used.contains(&nums[i]) && nums[i] >= *cur.last().unwrap() {
            used.insert(nums[i]);
            cur.push(nums[i]);
            dfs(nums, i+1, cur, total);
            cur.pop();
        }
    }
}

pub fn find_subsequences(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut cur = vec![MIN];
    let mut total: Vec<Vec<i32>> = vec![];
    dfs(&nums, 0, &mut cur, &mut total);
    total
}


#[test]
fn test_491() {
    assert_eq!(
        vec![vec![1, 2], vec![1, 1], vec![1, 1, 1], vec![1, 1, 1, 1]], find_subsequences(vec![1, 2, 1, 1, 1])
    );
}
