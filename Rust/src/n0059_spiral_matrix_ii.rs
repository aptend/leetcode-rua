pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
    let mut total = n;
    let mut m = vec![(1..=n).collect::<Vec<i32>>(); n as usize];
    let (mut i, mut j) = (0, n - 1);
    let mut cnt = n;
    let dirs = vec![(1, 0), (0, -1), (-1, 0), (0, 1)];
    while total < n * n {
        for (idx, (di, dj)) in dirs.iter().enumerate() {
            if idx == 0 || idx == 2 {
                cnt -= 1;
            }
            for _ in 0..cnt {
                i += di;
                j += dj;
                total += 1;
                m[i as usize][j as usize] = total;
            }
        }
    }
    m
}

#[test]
fn test_59() {
    assert_eq!(
        vec![vec![1, 2, 3], vec![8, 9, 4], vec![7, 6, 5]],
        generate_matrix(3)
    );
}
