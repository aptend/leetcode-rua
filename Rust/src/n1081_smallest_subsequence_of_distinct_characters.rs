pub fn smallest_subsequence(text: String) -> String {
    let mut last_index = std::collections::HashMap::new();
    for (i, ch) in text.chars().enumerate() {
        *last_index.entry(ch).or_insert(0) = i;
    }

    let mut stack: Vec<char> = vec![];
    let mut seen = std::collections::HashSet::new();
    for (i, ch) in text.chars().enumerate() {
        if seen.contains(&ch) {
            continue;
        }
        while !stack.is_empty()
            && *stack.last().unwrap() > ch
            && last_index[stack.last().unwrap()] > i
        {
            seen.remove(&stack.pop().unwrap());
        }
        stack.push(ch);
        seen.insert(ch);
    }
    stack.into_iter().collect()
}

#[test]
fn test_1081() {
    assert_eq!(
        "adbc".to_owned(),
        smallest_subsequence("cdadabcc".to_owned())
    );
    assert_eq!(
        "eacb".to_owned(),
        smallest_subsequence("ecbacba".to_owned())
    );
    assert_eq!(
        "ceab".to_owned(),
        smallest_subsequence("eceacba".to_owned())
    );
}
