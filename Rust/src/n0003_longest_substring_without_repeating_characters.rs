use std::cmp::max;
pub fn length_of_longest_substring(s: String) -> i32 {
    let mut seen = std::collections::HashMap::new();
    let mut j = 0;
    let mut ans = 0;
    for (i, ch) in s.chars().enumerate() {
        if seen.contains_key(&ch) {
            ans = max(ans, i as i32 - j);
            j = max(j, seen[&ch] + 1);
        }
        seen.insert(ch, i as i32);
    }
    ans = max(ans, s.len() as i32 - j);
    ans
}

#[test]
fn test_3() {
    assert_eq!(3, length_of_longest_substring("abcabcbb".to_owned()));
    assert_eq!(1, length_of_longest_substring("bbbbb".to_owned()));
    assert_eq!(3, length_of_longest_substring("pwwkew".to_owned()));
    assert_eq!(3, length_of_longest_substring("aabbaab!bb".to_owned()));
}
