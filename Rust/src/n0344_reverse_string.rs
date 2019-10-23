pub fn reverse_string(s: &mut Vec<char>) {
    if !s.is_empty() {
        let (mut i, mut j) = (0, s.len() - 1);
        while i < j {
            s.swap(i, j);
            i += 1;
            j -= 1;
        }
    }
}

#[test]
fn test_344() {
    let mut s = vec!['h', 'e', 'l', 'l', 'o'];
    reverse_string(&mut s);
    assert_eq!(vec!['o', 'l', 'l', 'e', 'h'], s);
}
