pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
    if s.len() < p.len() {
        return vec![];
    }
    let N = p.len();
    let mut map = [0; 26];
    let index_ch = |ch: char| ch as usize - 97;
    for ch in p.chars() {
        map[index_ch(ch)] += 1;
    }
    for ch in s.chars().take(N) {
        map[index_ch(ch)] -= 1;
    }
    let mut ans = vec![];
    let schars: Vec<char> = s.chars().collect();
    for i in 0..(s.len() - N) {
        if map.iter().all(|x| *x == 0) {
            ans.push(i as i32);
        }
        map[index_ch(schars[i])] += 1;
        map[index_ch(schars[i + N])] -= 1;
    }
    if map.iter().all(|x| *x == 0) {
        ans.push((s.len() - N) as i32);
    }
    ans
}

#[test]
fn test_438() {
    assert_eq!(
        Vec::<i32>::new(),
        find_anagrams("".to_owned(), "a".to_owned())
    );
    assert_eq!(
        vec![0, 6, 7],
        find_anagrams("cbaebabacb".to_owned(), "abc".to_owned())
    );
    assert_eq!(vec![1], find_anagrams("baa".to_owned(), "aa".to_owned()));
}
