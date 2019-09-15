pub fn reverse_parentheses(s: String) -> String {
    let mut stack: Vec<Vec<char>> = vec![vec![]];
    for ch in s.chars() {
        match ch {
            '(' => stack.push(vec![]),
            ')' => {
                let inner = stack.pop().unwrap();
                stack.last_mut().unwrap().extend(inner.iter().rev());
            }
            _ => stack.last_mut().unwrap().push(ch),
        }
    }
    stack.last().unwrap().iter().collect::<String>()
}

#[test]
fn test_1190() {
    assert_eq!("dcba", reverse_parentheses("(abcd)".to_owned()));
    assert_eq!("abc", reverse_parentheses("a()((bc))".to_owned()));
    assert_eq!("iloveu", reverse_parentheses("(u(love)i)".to_owned()));
    assert_eq!("leetcode", reverse_parentheses("(ed(et(oc))el)".to_owned()));
    assert_eq!(
        "apmnolkjihgfedcbq",
        reverse_parentheses("a(bcdefghijkl(mno)p)q".to_owned())
    );
}
