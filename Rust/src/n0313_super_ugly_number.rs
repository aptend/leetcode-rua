use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn nth_super_ugly_number(n: i32, primes: Vec<i32>) -> i32 {
    let mut heap = BinaryHeap::new();
    for &p in &primes {
        heap.push((Reverse(p), p, 1));
    }
    let mut ugly: Vec<i32> = vec![1];
    let mut cnt = 1;
    while cnt < n {
        let (Reverse(v), p, idx) = heap.pop().unwrap();
        if v > *ugly.last().unwrap() {
            ugly.push(v);
            cnt += 1;
        }
        heap.push((Reverse(p * ugly[idx]), p, idx + 1))
    }

    *ugly.last().unwrap()
}

#[test]
fn test_313() {
    assert_eq!(32, nth_super_ugly_number(12, vec![2, 7, 13, 19]));
}
