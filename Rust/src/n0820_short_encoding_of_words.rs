pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
    let mut w_set: std::collections::HashSet<String> = words.into_iter().collect();
    for w in w_set.clone().iter() {
        for i in 1..w.len() {
            w_set.remove(&w[i..]);
        }
    }
    w_set.iter().fold(0, |acc, x| acc + x.len() as i32 + 1)
}

#[test]
fn test_820() {
    assert_eq!(
        10,
        minimum_length_encoding(vec!["time".to_owned(), "me".to_owned(), "wall".to_owned()])
    );
}
