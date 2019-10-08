use std::collections::{HashSet, VecDeque};
pub fn racecar(target: i32) -> i32 {
    if target == 0 {
        return 0;
    }
    let mut q = VecDeque::new();
    q.push_back((0, 1));
    let mut turn_points = HashSet::new();
    turn_points.insert((0, 1));
    turn_points.insert((0, -1));
    let mut step = 0;
    while !q.is_empty() {
        step += 1;
        for _ in 0..q.len() {
            let (pos, v) = q.pop_front().unwrap();

            if pos + v == target {
                return step;
            }

            // just forward
            q.push_back((pos + v, v * 2));
            // take a turn
            let r_stat = (pos, if v > 0 { -1 } else { 1 });
            if !turn_points.contains(&r_stat) {
                turn_points.insert(r_stat);
                q.push_back(r_stat);
            }
        }
    }
    -1
}

#[test]
fn test_818() {
    assert_eq!(5, racecar(6));
    assert_eq!(2, racecar(3));
    assert_eq!(24, racecar(330));
}
