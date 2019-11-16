pub fn first_uniq_char(s: String) -> i32 {
    let ch_usizes: Vec<_> = s.chars().map(|ch| ch as usize - 97).collect();
    let mut i = 0;
    let mut counter = [0; 26];
    for ch in &ch_usizes {
        counter[*ch] += 1;
        while i < s.len() && counter[ch_usizes[i]] > 1 {
            i += 1;
        }
    }
    if i == s.len() {
        -1
    } else {
        i as i32
    }
}

#[test]
fn test_387() {
    assert_eq!(0, first_uniq_char("leetcode".to_owned()));
    assert_eq!(2, first_uniq_char("loveleetcode".to_owned()));
}
