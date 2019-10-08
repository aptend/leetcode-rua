pub fn count_binary_substrings(s: String) -> i32 {
    let (mut cnt0, mut cnt1, mut prev, mut ans) = (0, 0, ' ', 0);
    for x in s.chars() {
        if x != prev {
            ans += std::cmp::min(cnt0, cnt1);
            match x {
                '1' => cnt1 = 0,
                _ => cnt0 = 0,
            }
        }
        match x {
            '1' => cnt1 += 1,
            _ => cnt0 += 1,
        }
        prev = x;
    }
    ans += std::cmp::min(cnt0, cnt1);
    ans
}

#[test]
fn test_696() {
    assert_eq!(6, count_binary_substrings("00110011".to_owned()));
    assert_eq!(4, count_binary_substrings("10101".to_owned()));
}
