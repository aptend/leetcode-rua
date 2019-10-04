use std::collections::HashMap;
pub fn reordered_power_of2(n: i32) -> bool {
    let n_str = n.to_string();
    let mut n_stat = HashMap::new();
    for p in n_str.chars() {
        *n_stat.entry(p).or_insert(0) += 1;
    }
    let mut x = 1;
    while x < 1e9 as i32{
        let x_str = x.to_string();
        let mut x_stat = HashMap::new();
        for p in x_str.chars() {
           *x_stat.entry(p).or_insert(0) += 1;
        }
        if n_stat == x_stat {
            return true;
        }
        x <<= 1;
    }
    false
}

#[test]
fn test_869() {
    assert_eq!(true, reordered_power_of2(1));
    assert_eq!(true, reordered_power_of2(46));
    assert_eq!(false, reordered_power_of2(373));
}
