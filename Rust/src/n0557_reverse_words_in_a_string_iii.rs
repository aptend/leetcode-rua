pub fn reverse_words(s: String) -> String {
    s.split(' ')
        .map(|p| p.chars().rev().collect::<String>())
        .collect::<Vec<String>>()
        .join(" ")
}

#[test]
fn test_557() {
    assert_eq!(
        "s'teL ekat edoCteeL tsetnoc".to_owned(),
        reverse_words("Let's take LeetCode contest".to_owned())
    )
}
