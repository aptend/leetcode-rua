#[allow(clippy::many_single_char_names)]
pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
    if matrix.is_empty() {
        return vec![];
    }
    let (m, n) = (matrix.len() as i32, matrix[0].len() as i32);
    let mut ans = matrix[0].clone();
    let mut total = n;
    let (mut i, mut j) = (0, n - 1);
    let mut k = 0;
    let dirs = vec![(1, 0), (0, -1), (-1, 0), (0, 1)];
    'out: loop {
        for (idx, (di, dj)) in dirs.iter().enumerate() {
            if idx == 0 || idx == 2 {
                k += 1;
            }
            let cnt = if idx % 2 == 0 { m - k } else { n - k };
            for _ in 0..cnt {
                i += di;
                j += dj;
                total += 1;
                ans.push(matrix[i as usize][j as usize]);
            }
            if total == m * n {
                break 'out;
            }
        }
    }
    ans
}

#[test]
fn test_54() {
    assert_eq!(
        vec![1, 2, 3, 6, 9, 8, 7, 4, 5],
        spiral_order(vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]])
    );
}
