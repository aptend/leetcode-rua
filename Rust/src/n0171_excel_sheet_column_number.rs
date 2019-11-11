pub fn title_to_number(s: String) -> i32 {
    s.chars()
        .fold(0, |a, ch| 26 * a + ch as i32 - 'A' as i32 + 1)
}

#[test]
fn test_171() {
    assert_eq!(701, title_to_number("ZY".to_owned()));
    assert_eq!(1, title_to_number("A".to_owned()));
}
