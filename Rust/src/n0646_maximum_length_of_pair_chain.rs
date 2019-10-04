use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn find_longest_chain_heap(pairs: Vec<Vec<i32>>) -> i32 {
    let mut heap = BinaryHeap::new();
    for p in &pairs {
        heap.push(Reverse((p[1], p[0])));
    }
    let mut lower = std::i32::MIN;
    let mut cnt = 0;
    while !heap.is_empty() {
        let Reverse((a, b)) = heap.pop().unwrap();
        if b > lower {
            cnt += 1;
            lower = a;
        }
    }
    cnt
}

pub fn find_longest_chain(pairs: Vec<Vec<i32>>) -> i32 {
    let mut pairs = pairs;
    pairs.sort_by_key(|p| p[1]);
    let mut lower = std::i32::MIN;
    let mut cnt = 0;
    for p in &pairs {
        if p[0] > lower {
            cnt += 1;
            lower = p[1];
        }
    }
    cnt
}

#[test]
fn test_646() {
    assert_eq!(
        3,
        find_longest_chain(vec![vec![1, 2], vec![3, 4], vec![5, 6]])
    );
    assert_eq!(
        2,
        find_longest_chain(vec![vec![1, 2], vec![2, 3], vec![3, 4]])
    );
    assert_eq!(
        2,
        find_longest_chain(vec![vec![3, 4], vec![2, 3], vec![1, 2]])
    );
    assert_eq!(
        4,
        find_longest_chain(vec![
            vec![-10, -8],
            vec![8, 9],
            vec![-5, 0],
            vec![6, 10],
            vec![-6, -4],
            vec![1, 7],
            vec![9, 10],
            vec![-4, 7]
        ])
    )
}
