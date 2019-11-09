pub fn min_window(s: String, t: String) -> String {
    let mut count = std::collections::HashMap::new();
    for ch in t.chars() {
        *count.entry(ch).or_insert(0) += 1;
    }
    let mut formed = 0;
    let mut i = 0;
    let mut ans = None;
    let mut length = s.len() + 1;
    let schars: Vec<_> = s.chars().collect();
    for (j, ch) in schars.iter().enumerate() {
        if count.contains_key(ch) {
            *count.get_mut(ch).unwrap() -= 1;
            formed += if count[ch] == 0 { 1 } else { 0 }
        }
        while formed == count.len() {
            if (j - i) < length {
                ans = Some((i, j));
                length = j - i;
            }
            let ich = &schars[i];
            if count.contains_key(ich) {
                *count.get_mut(ich).unwrap() += 1;
                formed -= if count[ich] > 0 { 1 } else { 0 }
            }
            i += 1;
        }
    }
    ans.map(|r| schars[r.0..=r.1].iter().collect())
        .unwrap_or_else(|| "".to_owned())
}

#[test]
fn test_76() {
    assert_eq!(
        "BANC".to_owned(),
        min_window("ADOBECODEBANC".to_owned(), "ABC".to_owned())
    );
    assert_eq!(
        "".to_owned(),
        min_window("ADOBECODEBANC".to_owned(), "ABCT".to_owned())
    );
    assert_eq!(
        "aa".to_owned(),
        min_window("aa".to_owned(), "aa".to_owned())
    );
}
