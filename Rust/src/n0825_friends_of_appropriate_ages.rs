use crate::bisect::Bisect;

pub fn num_friend_requests(ages: Vec<i32>) -> i32 {
    let mut ages = ages;
    ages.sort_unstable();
    let mut ans = 0;
    for &a in &ages {
        let lower = a / 2 + 7;
        let j = ages.bisect_right(lower);
        let i = ages.bisect_right(a);
        if i > j {
            ans += i - j - 1;
        }
    }
    ans as i32
}

#[test]
fn test_825() {
    assert_eq!(3, num_friend_requests(vec![5, 24, 82, 108, 115]));
    assert_eq!(2, num_friend_requests(vec![16, 16]));
    assert_eq!(2, num_friend_requests(vec![16, 17, 18]));
    assert_eq!(3, num_friend_requests(vec![20, 30, 100, 110, 120]));
}

// fn bisect_r(hay: &[i32], needle: i32) -> usize {
//     let mut i = 0i32;
//     let mut j = (hay.len() - 1) as i32;
//     while i <= j {
//         let mid = i + (j - i) / 2;
//         if hay[mid as usize] > needle {
//             j = mid - 1;
//         } else {
//             i = mid + 1;
//         }
//     }
//     i as usize
// }
