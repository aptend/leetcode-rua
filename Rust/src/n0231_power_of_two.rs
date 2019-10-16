pub fn is_power_of_two(n: i32) -> bool {
    n.is_positive() && n.count_ones() == 1
}

#[test]
fn test_231() {
    assert_eq!(false, is_power_of_two(0));
    assert_eq!(false, is_power_of_two(-64));
    assert_eq!(false, is_power_of_two(2414));
    assert_eq!(true, is_power_of_two(1024));
}
