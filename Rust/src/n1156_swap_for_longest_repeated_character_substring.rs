use std::cmp::max;
pub fn max_rep_opt1(text: String) -> i32 {
    let mut counter = [0; 26];
    let mut win_cnt = [0; 26];
    let index_ch = |x: char| x as usize - 97;
    for ch in text.chars() {
        counter[index_ch(ch)] += 1;
    }
    let tchars: Vec<char> = text.chars().collect();
    let mut max_char = 'x';
    let mut max_freq = 0;
    let mut i = 0;
    let mut ans = 0;
    for j in 0..tchars.len() {
        let ch = tchars[j];
        let ich = index_ch(ch);
        win_cnt[ich] += 1;
        if win_cnt[ich] > max_freq {
            max_char = ch;
            max_freq = win_cnt[ich];
        }
        while j - i + 1 - max_freq > 1 {
            if counter[index_ch(max_char)] > max_freq {
                ans = max(ans, j - i);
            } else {
                ans = max(ans, max_freq);
            }
            win_cnt[index_ch(tchars[i])] -= 1;
            i += 1;
        }
    }

    if counter[index_ch(max_char)] > max_freq {
        ans = max(ans, tchars.len() - i);
    } else {
        ans = max(ans, max_freq);
    }
    ans as i32
}

#[test]
fn test_1156() {
    assert_eq!(1, max_rep_opt1("abcdef".to_owned()));
    assert_eq!(3, max_rep_opt1("ababa".to_owned()));
    assert_eq!(6, max_rep_opt1("aaabaaa".to_owned()));
    assert_eq!(4, max_rep_opt1("aaabbaaa".to_owned()));
    assert_eq!(5, max_rep_opt1("aaaaa".to_owned()));
    assert_eq!(9, max_rep_opt1("aaabbcbbbabbbbb".to_owned()));
    assert_eq!(0, max_rep_opt1("".to_owned()));
    assert_eq!(6, max_rep_opt1("bbababaaaa".to_owned()));
}
