pub fn count_substrings_1(s: String) -> i32 {
    let N = s.len();
    let schars: Vec<_> = s.chars().collect();
    let mut dp = vec![vec![false; N]; N];
    for gap in 0..N {
        for i in 0..(N - gap) {
            if gap == 0 || (schars[i] == schars[i + gap] && (gap == 1 || dp[i + 1][i + gap - 1])) {
                dp[i][i + gap] = true;
            }
        }
    }

    dp.into_iter().flatten().filter(|&x| x).count() as i32
}

pub fn count_substrings(s: String) -> i32 {
    let N = s.len();
    let schars: Vec<_> = s.chars().collect();
    let mut dp = vec![vec![false; N]; N];
    for j in 0..N {
        for i in 0..=j {
            if i == j || (schars[i] == schars[j] && (i + 1 == j || dp[i + 1][j - 1])) {
                dp[i][j] = true;
            }
        }
    }
    dp.into_iter().flatten().filter(|&x| x).count() as i32
}

#[test]
fn test_647() {
    assert_eq!(0, count_substrings("".to_owned()));
    assert_eq!(3, count_substrings("abc".to_owned()));
    assert_eq!(6, count_substrings("aaa".to_owned()));
}
