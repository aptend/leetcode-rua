pub fn longest_palindrome(s: String) -> String {
    if s.is_empty() {
        return "".to_owned();
    }
    let mut ans = (0, 0);
    let mut l = 0;
    let Ni32 = s.len() as i32;
    let chars: Vec<_> = s.chars().collect();
    let mut expand = |mut i, mut j| {
        while i >= 0 && j < Ni32 && chars[i as usize] == chars[j as usize] {
            i -= 1;
            j += 1;
        }
        if j - i - 1 > l {
            l = j - i - 1;
            ans = (i + 1, j - 1);
        }
    };

    for i in 0..Ni32 {
        expand(i, i);
        expand(i, i + 1);
    }
    s[ans.0 as usize..=ans.1 as usize].to_owned()
}

#[test]
fn test_5() {
    assert_eq!("bab".to_owned(), longest_palindrome("babad".to_owned()));
    assert_eq!("bb".to_owned(), longest_palindrome("cbbd".to_owned()));
    assert_eq!("".to_owned(), longest_palindrome("".to_owned()));
}
