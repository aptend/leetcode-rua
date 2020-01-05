pub fn is_match(s: String, p: String) -> bool {
    fn re_match(s: &[char], p: &[char], i: usize, j: usize, memo: &mut Vec<Vec<i32>>) -> bool {
        if j >= p.len() {
            return i == s.len();
        }
        if memo[i][j] != 0 {
            return memo[i][j] > 0;
        }
        let mut ans = false;
        let first_match = i < s.len() && (s[i] == p[j] || p[j] == '.');
        if j < p.len() - 1 && p[j + 1] == '*' {
            ans = re_match(s, p, i, j + 2, memo);
            if first_match {
                ans = ans || re_match(s, p, i + 1, j, memo) || re_match(s, p, i + 1, j + 2, memo);
            }
        } else if first_match {
            ans = re_match(s, p, i + 1, j + 1, memo);
        }
        memo[i][j] = if ans { 1 } else { -1 };
        ans
    }
    let schs: Vec<char> = s.chars().collect();
    let pchs: Vec<char> = p.chars().collect();
    let mut memo = vec![vec![0; pchs.len() + 1]; schs.len() + 1];
    return re_match(&schs, &pchs, 0, 0, &mut memo);
}

#[test]
fn test_10() {
    assert!(is_match("a".to_owned(), "ab*".to_owned()));
    assert!(is_match("aab".to_owned(), "c*a*b".to_owned()));
    assert!(is_match("ab".to_owned(), "a*ab".to_owned()));
    assert!(!is_match("".to_owned(), ".".to_owned()));
    assert!(!is_match("aa".to_owned(), "a".to_owned()));
    assert!(is_match("aa".to_owned(), "a*".to_owned()));
    assert!(is_match("ab".to_owned(), ".*".to_owned()));
    assert!(!is_match("mississippi".to_owned(), "mis*is*p*.".to_owned()));
}
