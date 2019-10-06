pub fn min_cost_to_move_chips(chips: Vec<i32>) -> i32 {
    std::cmp::min(
        chips.iter().filter(|&x| x % 2 == 1).count(),
        chips.iter().filter(|&x| x % 2 == 0).count(),
    ) as i32
}

#[test]
fn test_1217() {
    assert_eq!(2, min_cost_to_move_chips(vec![2, 2, 2, 3, 3]));
    assert_eq!(1, min_cost_to_move_chips(vec![1, 2, 3]));
}
