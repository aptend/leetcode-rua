pub fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut stack = vec![];
    for ch in &tokens {
        match &ch[..] {
            "+" => {
                let op1 = stack.pop().unwrap();
                let op2 = stack.pop().unwrap();
                stack.push(op1 + op2);
            }
            "-" => {
                let op1 = stack.pop().unwrap();
                let op2 = stack.pop().unwrap();
                stack.push(op2 - op1);
            }
            "*" => {
                let op1 = stack.pop().unwrap();
                let op2 = stack.pop().unwrap();
                stack.push(op1 * op2);
            }
            "/" => {
                let op1 = stack.pop().unwrap();
                let op2 = stack.pop().unwrap();
                stack.push(op2 / op1);
            }

            _ => stack.push(ch.parse::<i32>().unwrap()),
        }
    }
    stack[0]
}

#[test]
fn test_150() {
    assert_eq!(
        22,
        eval_rpn(vec![
            "10".to_owned(),
            "6".to_owned(),
            "9".to_owned(),
            "3".to_owned(),
            "+".to_owned(),
            "-11".to_owned(),
            "*".to_owned(),
            "/".to_owned(),
            "*".to_owned(),
            "17".to_owned(),
            "+".to_owned(),
            "5".to_owned(),
            "+".to_owned()
        ])
    );
}
