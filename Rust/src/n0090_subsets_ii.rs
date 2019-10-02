// use std::collections::HashSet;
pub fn dfs(nums: &Vec<i32>, start: usize, cur: &mut Vec<i32>, total: &mut Vec<Vec<i32>>) {
    total.push(cur.clone());
    // let mut used = HashSet::new();
    for i in start..nums.len() {
        // if used.contains(&nums[i]) {
        //     continue;
        // }
        // used.insert(nums[i]);
        if i > start && nums[i] == nums[i-1] { continue }
        cur.push(nums[i]);
        dfs(nums, i+1, cur, total);
        cur.pop();
    }
}

pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut nums = nums;
    nums.sort_unstable();
    let mut cur = vec![];
    let mut total = vec![];
    dfs(&nums, 0, &mut cur, &mut total);
    total
}

#[test]
fn test_90() {
    assert_eq!(vec![vec![], vec![1], vec![1,1]], subsets_with_dup(vec![1, 1]));
}
