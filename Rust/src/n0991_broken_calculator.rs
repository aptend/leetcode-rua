pub fn broken_calc(x: i32, y: i32) -> i32 {
    if x >= y {
        x - y
    } else {
        1 + broken_calc(x, if y % 2 == 0 { y / 2 } else { y + 1 })
    }
}

#[test]
fn test_991() {
    assert_eq!(2, broken_calc(5, 8));
    assert_eq!(1023, broken_calc(1024, 1));
}
