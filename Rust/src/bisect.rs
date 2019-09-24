#![allow(unused)]
use std::cmp::Ordering::{Greater, Less};
use std::cmp::PartialOrd;

trait Bisect {
    type Item;
    fn bisect_right(&self, target: Self::Item) -> usize;
    fn bisect_left(&self, target: Self::Item) -> usize;
}

impl<T: PartialOrd> Bisect for [T] {
    type Item = T;
    fn bisect_right(&self, target: T) -> usize {
        self.binary_search_by(|x| if *x > target { Greater } else { Less })
            .unwrap_err()
    }
    fn bisect_left(&self, target: T) -> usize {
        self.binary_search_by(|x| if *x >= target { Greater } else { Less })
            .unwrap_err()
    }
}

#[test]
fn test_bisect() {
    let hay = vec![1, 1, 1, 2, 2, 2, 5, 5, 5];
    assert_eq!(0, hay.bisect_right(0));
    assert_eq!(3, hay.bisect_right(1));
    assert_eq!(0, hay.bisect_left(1));
    assert_eq!(3, hay.bisect_left(2));
    assert_eq!(6, hay.bisect_right(2));
    assert_eq!(6, hay.bisect_right(4));
    assert_eq!(6, hay.bisect_left(3));
    assert_eq!(6, hay.bisect_left(5));
    assert_eq!(9, hay.bisect_right(5));
    assert_eq!(9, hay.bisect_right(7));
}
