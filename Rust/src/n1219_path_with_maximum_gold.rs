#[allow(clippy::many_single_char_names)]
pub fn get_maximum_gold(grid: Vec<Vec<i32>>) -> i32 {
    fn dfs(i: i32, j: i32, amount: i32, gmax: &mut i32, g: &mut Vec<Vec<i32>>) {
        let m = g.len() as i32;
        let n = g[0].len() as i32;
        for (di, dj) in &[(1, 0), (-1, 0), (0, 1), (0, -1)] {
            let (ni, nj) = (i + di, j + dj);
            if ni >= 0 && ni < m && nj >= 0 && nj < n && g[ni as usize][nj as usize] != 0 {
                let tmp = g[ni as usize][nj as usize];
                g[ni as usize][nj as usize] = 0;
                dfs(ni, nj, amount + tmp, gmax, g);
                g[ni as usize][nj as usize] = tmp;
            } else {
                *gmax = std::cmp::max(*gmax, amount);
            }
        }
    }
    let mut ans = 0;
    let mut grid = grid;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            let tmp = grid[i as usize][j as usize];
            if tmp != 0 {
                grid[i as usize][j as usize] = 0;
                dfs(i as i32, j as i32, tmp, &mut ans, &mut grid);
                grid[i as usize][j as usize] = tmp;
            }
        }
    }
    ans
}

#[test]
fn test_1219() {
    assert_eq!(
        24,
        get_maximum_gold(vec![vec![0, 6, 0], vec![5, 8, 7], vec![0, 9, 0]])
    );
    assert_eq!(
        28,
        get_maximum_gold(vec![
            vec![1, 0, 7],
            vec![2, 0, 6],
            vec![3, 4, 5],
            vec![0, 3, 0],
            vec![9, 0, 20]
        ])
    )
}
