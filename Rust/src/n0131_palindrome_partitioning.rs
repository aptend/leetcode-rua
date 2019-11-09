pub fn partition(s: String) -> Vec<Vec<String>> {
    let N = s.len();
    let chs: Vec<_> = s.chars().collect();
    let mut dp = vec![vec![false; N]; N];
    for gap in 0..N {
        for i in 0..(N - gap) {
            if gap == 0 || (chs[i] == chs[i + gap] && (gap == 1 || dp[i + 1][i + gap - 1])) {
                dp[i][i + gap] = true;
            }
        }
    }
    fn dfs(
        chs: &[char],
        start: usize,
        dp: &[Vec<bool>],
        cur: &mut Vec<String>,
        total: &mut Vec<Vec<String>>,
    ) {
        if start >= chs.len() {
            total.push(cur.clone());
        } else {
            for i in start..chs.len() {
                if dp[start][i] {
                    cur.push(chs[start..=i].iter().collect());
                    dfs(chs, i + 1, dp, cur, total);
                    cur.pop().unwrap();
                }
            }
        }
    }
    let mut cur = vec![];
    let mut total = vec![];
    dfs(&chs, 0, &dp, &mut cur, &mut total);
    total
}

#[test]
fn test_131() {
    assert_eq!(
        vec![
            vec!["a".to_owned(), "a".to_owned(), "b".to_owned()],
            vec!["aa".to_owned(), "b".to_owned()]
        ],
        partition("aab".to_owned())
    );
}
