use std::cmp::max;
use std::collections::HashSet;

pub fn arrays_intersection_hashset(arr1: Vec<i32>, arr2: Vec<i32>, arr3: Vec<i32>) -> Vec<i32> {
    let a1: HashSet<i32> = arr1.into_iter().collect();
    let a2: HashSet<i32> = arr2.into_iter().collect();
    let a3: HashSet<i32> = arr3.into_iter().collect();
    let mut a = a1
        .intersection(&a2)
        .cloned()
        .collect::<HashSet<i32>>()
        .intersection(&a3)
        .cloned()
        .collect::<Vec<i32>>();
    a.sort_unstable();
    a
}

pub fn arrays_intersection(arr1: Vec<i32>, arr2: Vec<i32>, arr3: Vec<i32>) -> Vec<i32> {
    let (mut i1, mut i2, mut i3) = (0, 0, 0);
    let mut ans = vec![];
    while i1 < arr1.len() && i2 < arr2.len() && i3 < arr3.len() {
        let (v1, v2, v3) = (arr1[i1], arr2[i2], arr3[i3]);
        if v1 == v2 && v2 == v3 {
            ans.push(v1);
            i1 += 1;
            i2 += 1;
            i3 += 1;
            continue;
        }
        let m = max(v1, max(v2, v3));
        if v1 < m {
            i1 += 1;
        }
        if v2 < m {
            i2 += 1;
        }
        if v3 < m {
            i3 += 1;
        }
    }
    ans
}

#[test]
fn test_1213() {
    assert_eq!(
        vec![1, 5],
        arrays_intersection(
            vec![1, 2, 3, 4, 5],
            vec![1, 2, 5, 7, 9],
            vec![1, 3, 4, 5, 8]
        )
    );
}
