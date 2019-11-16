pub fn fizz_buzz(n: i32) -> Vec<String> {
    fn fibu(n: i32) -> String {
        let mut base = String::new();
        if n % 3 == 0 {
            base.push_str("Fizz");
        }
        if n % 5 == 0 {
            base.push_str("Buzz");
        }
        if base.is_empty() {
            base.push_str(&format!("{}", n));
        }
        base
    }
    (1..=n).map(fibu).collect()
}

#[test]
fn test_412() {
    assert_eq!(
        vec![
            "1".to_owned(),
            "2".to_owned(),
            "Fizz".to_owned(),
            "4".to_owned(),
            "Buzz".to_owned(),
            "Fizz".to_owned(),
            "7".to_owned(),
            "8".to_owned(),
            "Fizz".to_owned(),
            "Buzz".to_owned(),
            "11".to_owned(),
            "Fizz".to_owned(),
            "13".to_owned(),
            "14".to_owned(),
            "FizzBuzz".to_owned(),
        ],
        fizz_buzz(15)
    );
}
