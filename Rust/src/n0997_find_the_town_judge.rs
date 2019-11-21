pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
    let mut candidates = vec![true; n as usize + 1];
    let mut votes = vec![0i32; n as usize + 1];
    for t in &trust {
        candidates[t[0] as usize] = false;
        votes[t[1] as usize] += 1;
    }
    for i in 1..candidates.len() {
        if candidates[i] && votes[i] == n - 1 {
            return i as i32;
        }
    }
    -1
}

#[test]
fn test_997() {
    assert_eq!(2, find_judge(2, vec![vec![1, 2]]));
    assert_eq!(3, find_judge(3, vec![vec![1, 3], vec![2, 3]]));
    assert_eq!(-1, find_judge(3, vec![vec![1, 3], vec![2, 3], vec![3, 1]]));
}
