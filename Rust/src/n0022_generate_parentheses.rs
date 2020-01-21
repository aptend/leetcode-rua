fn gen(n: i32, left: i32, form: &mut String, ans: &mut Vec<String>) {
    if n == 0 {
        ans.push(form.clone());
        return;
    }
    if left < n {
        form.push('(');
        gen(n, left + 1, form, ans);
        form.pop().unwrap();
    }
    if left > 0 {
        form.push(')');
        gen(n - 1, left - 1, form, ans);
        form.pop().unwrap();
    }
}
pub fn generate_parenthesis(n: i32) -> Vec<String> {
    let mut ans = vec![];
    let mut form = String::new();
    gen(n, 0, &mut form, &mut ans);
    ans
}

#[test]
fn test_22() {
    assert_eq!(
        generate_parenthesis(3),
        vec![
            "((()))".to_owned(),
            "(()())".to_owned(),
            "(())()".to_owned(),
            "()(())".to_owned(),
            "()()()".to_owned()
        ]
    );
}
