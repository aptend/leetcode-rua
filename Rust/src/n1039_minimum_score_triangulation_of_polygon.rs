pub fn min_score_triangulation(a: Vec<i32>) -> i32 {
    let N = a.len();
    let mut memo = vec![vec![None; N]; N];
    fn solve(a: &[i32], memo: &mut Vec<Vec<Option<i32>>>, i: usize, j: usize) -> i32 {
        if j - i <= 1 {
            return 0;
        }
        if let Some(x) = memo[i][j] {
            return x;
        }
        let base = a[i] * a[j];
        let ans = (i + 1..j)
            .map(|k| solve(a, memo, i, k) + solve(a, memo, k, j) + base * a[k])
            .min()
            .unwrap();
        memo[i][j] = Some(ans);
        ans
    }
    solve(&a, &mut memo, 0, N - 1)
}

#[test]
fn test_1039() {
    assert_eq!(6, min_score_triangulation(vec![1, 2, 3]));
    assert_eq!(144, min_score_triangulation(vec![3, 7, 4, 5]));
    assert_eq!(13, min_score_triangulation(vec![1, 3, 1, 4, 1, 5]));
}
