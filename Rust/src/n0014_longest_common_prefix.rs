pub fn longest_common_prefix(strs: Vec<String>) -> String {
    if strs.is_empty() {
        return "".to_owned();
    } else if strs.len() == 1 {
        return strs[0].clone();
    }
    let mut str_iters: Vec<_> = strs.iter().map(|s| s.chars()).collect();
    let mut ans = vec![];
    'outer: loop {
        let ch = str_iters[0].next().unwrap_or('-');
        if ch == '-' {
            break;
        }
        for iter in str_iters.iter_mut().skip(1) {
            let cur = iter.next().unwrap_or('-');
            if cur == '-' || cur != ch {
                break 'outer;
            }
        }
        ans.push(ch);
    }
    ans.into_iter().collect::<String>()
}

#[test]
fn test_14() {
    assert_eq!(
        "flower".to_owned(),
        longest_common_prefix(vec!["flower".to_owned()])
    );
    assert_eq!(
        "".to_owned(),
        longest_common_prefix(vec!["time".to_owned(), "flower".to_owned()])
    );
    assert_eq!(
        "fl".to_owned(),
        longest_common_prefix(vec!["flee".to_owned(), "flower".to_owned()])
    );
}
