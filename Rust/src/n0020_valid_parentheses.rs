pub fn is_valid(s: String) -> bool {
    let mut map = std::collections::HashMap::new();
    map.insert(')', '(');
    map.insert(']', '[');
    map.insert('}', '{');
    let mut stack = vec![];
    for ch in s.chars() {
        match ch {
            '(' | '{' | '[' => stack.push(ch),
            _ => {
                if stack.is_empty() || stack.pop().unwrap() != map[&ch] {
                    return false;
                }
            }
        }
    }
    stack.is_empty()
}

#[test]
fn test_20() {
    assert_eq!(true, is_valid("()[]{}".to_owned()));
    assert_eq!(false, is_valid("(}".to_owned()));
    assert_eq!(false, is_valid("(".to_owned()));
    assert_eq!(true, is_valid("([])".to_owned()));
}
