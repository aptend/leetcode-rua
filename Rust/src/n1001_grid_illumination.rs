use std::collections::{HashMap, HashSet};

#[allow(unused_variables)]
pub fn grid_illumination(n: i32, lamps: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
    let mut lamps: HashSet<Vec<i32>> = lamps.into_iter().collect();
    let mut ray_row = HashMap::new();
    let mut ray_col = HashMap::new();
    let mut ray_slash = HashMap::new();
    let mut ray_bslash = HashMap::new();
    for l in &lamps {
        let (i, j) = (l[0], l[1]);
        *ray_row.entry(i).or_insert(0) += 1;
        *ray_col.entry(j).or_insert(0) += 1;
        *ray_slash.entry(i + j).or_insert(0) += 1;
        *ray_bslash.entry(j - i).or_insert(0) += 1;
    }
    let mut ans = vec![];
    let dxs = [0, 1, 1, 1, -1, -1, -1, 0, 0];
    let dys = [0, 1, -1, 0, 0, 1, -1, 1, -1];
    for q in &queries {
        let (i, j) = (q[0], q[1]);
        if *ray_row.entry(i).or_default()
            + *ray_col.entry(j).or_default()
            + *ray_slash.entry(i + j).or_default()
            + *ray_bslash.entry(j - i).or_default()
            > 0
        {
            ans.push(1);
        } else {
            ans.push(0);
        }
        for (dx, dy) in dxs.iter().zip(dys.iter()) {
            let (ni, nj) = (i + dx, j + dy);
            let k = vec![ni, nj];
            if lamps.remove(&k) {
                *ray_row.entry(ni).or_insert(1) -= 1;
                *ray_col.entry(nj).or_insert(1) -= 1;
                *ray_slash.entry(ni + nj).or_insert(1) -= 1;
                *ray_bslash.entry(nj - ni).or_insert(1) -= 1;
            }
        }
    }
    ans
}

#[test]
fn test_1001() {
    assert_eq!(
        vec![1, 0],
        grid_illumination(
            5,
            vec![vec![0, 0], vec![4, 4]],
            vec![vec![1, 1], vec![1, 0]]
        )
    );
}
