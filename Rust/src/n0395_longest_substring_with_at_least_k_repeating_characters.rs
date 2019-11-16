fn longest(s: &str, k: i32) -> i32 {
    if s.is_empty() {
        return 0;
    }
    let mut counter = [0; 26];
    let idx_ch = |x| x as usize - 97;
    for ch in s.chars() {
        counter[idx_ch(ch)] += 1;
    }
    let query = |ch| counter[idx_ch(ch)] < k;
    let parts: Vec<_> = s.split(query).collect();
    if parts.len() == 1 {
        return s.len() as i32;
    }
    parts.into_iter().map(|p| longest(p, k)).max().unwrap()
}

pub fn longest_substring(s: String, k: i32) -> i32 {
    longest(&s, k)
}

#[test]
fn test_395() {
    assert_eq!(3, longest_substring("aaabb".to_owned(), 3));
    assert_eq!(5, longest_substring("ababbc".to_owned(), 2));
}
