use std::collections::{HashMap, HashSet};

#[allow(clippy::map_entry)]
pub fn word_pattern(pattern: String, str: String) -> bool {
    let word_list: Vec<&str> = str.split(' ').collect();
    if pattern.len() != word_list.len() {
        return false;
    }

    let mut memo = HashMap::new();
    let mut words = HashSet::new();
    for (p, s) in pattern.chars().zip(word_list) {
        if !memo.contains_key(&p) {
            if words.contains(s) {
                return false;
            } else {
                memo.insert(p, s);
                words.insert(s);
            }
        } else if memo[&p] != s {
            return false;
        }
    }

    true
}

#[test]
fn test_290() {
    assert_eq!(
        true,
        word_pattern("abba".to_owned(), "ac ba ba ac".to_owned())
    );
}
