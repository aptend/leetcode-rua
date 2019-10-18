use std::cmp::Reverse;
use std::collections::BinaryHeap;
pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    let k = k as usize;
    if k < nums.len() / 2 {
        let mut heap = BinaryHeap::new();
        for (i, &x) in nums.iter().enumerate() {
            heap.push(Reverse(x));
            if i >= k {
                heap.pop();
            }
        }
        let Reverse(x) = *heap.peek().unwrap();
        x
    } else {
        let mut heap = BinaryHeap::new();
        let rk = nums.len() - k;
        for (i, &x) in nums.iter().enumerate() {
            heap.push(x);
            if i > rk {
                heap.pop();
            }
        }
        *heap.peek().unwrap()
    }
}

#[test]
fn test_215() {
    assert_eq!(4, find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4));
    assert_eq!(5, find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2));
    assert_eq!(1, find_kth_largest(vec![3, 2, 1, 5, 6, 4], 6));
}
