pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
    let m = matrix.len();
    if m == 0 {
        return;
    }
    let n = matrix[0].len();
    if n == 0 {
        return;
    }
    let mut m_row = false;
    let mut m_col = false;
    for i in 0..m {
        for j in 0..n {
            if matrix[i][j] == 0 {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
                if i == 0 {
                    m_row = true;
                }
                if j == 0 {
                    m_col = true;
                }
            }
        }
    }
    for i in 1..m {
        for j in 1..n {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0;
            }
        }
    }
    if m_row {
        for j in 0..n {
            matrix[0][j] = 0;
        }
    }
    if m_col {
        for i in 0..m {
            matrix[i][0] = 0;
        }
    }
}

#[test]
fn test_73() {
    let mut m = vec![vec![0, 1, 2, 0], vec![3, 4, 5, 2], vec![1, 3, 1, 5]];
    set_zeroes(&mut m);
    assert_eq!(
        vec![vec![0, 0, 0, 0], vec![0, 4, 5, 0], vec![0, 3, 1, 0]],
        m
    );
}
