pub fn multiply(num1: String, num2: String) -> String {
    let a: Vec<char> = num1.chars().collect();
    let b: Vec<char> = num2.chars().collect();
    let mut ans = vec![0; a.len() + b.len()];
    for i in (0..a.len()).rev() {
        for j in (0..b.len()).rev() {
            let x = a[i].to_digit(10).unwrap() * b[j].to_digit(10).unwrap();
            let sum = ans[i + j + 1] + x;
            ans[i + j + 1] = sum % 10;
            ans[i + j] += sum / 10;
        }
    }
    let some = ans
        .into_iter()
        .skip_while(|p| p == &0)
        .map(|p| p.to_string())
        .collect::<String>();
    if some.is_empty() {
        "0".to_owned()
    } else {
        some
    }
}

#[test]
fn test_43() {
    assert_eq!("56088", multiply("123".to_owned(), "456".to_owned()));
    assert_eq!("0", multiply("0".to_owned(), "0".to_owned()));
}
