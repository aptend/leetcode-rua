pub fn gcd_of_strings(str1: String, str2: String) -> String {
    if str1.clone() + &str2 != str2.clone() + &str1 {
        "".to_owned()
    } else {
        let mut a = str1.len();
        let mut b = str2.len();
        while b > 0 {
            let tmp = a % b;
            a = b;
            b = tmp;
        }
        str1[..a].into()
    }
}

#[test]
fn test_1071() {
    assert_eq!(
        "AB".to_owned(),
        gcd_of_strings("ABABAB".to_owned(), "ABAB".to_owned())
    );
}
