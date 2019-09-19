pub fn can_make_pali_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
    let mut ans: Vec<bool> = vec![];
    let mut map: Vec<u32> = vec![0; s.len() + 1];
    let mut tmp: u32 = 0;
    for (i, ch) in (1..).zip(s.chars()) {
        tmp ^= 1 << (ch as u8 - 'a' as u8);
        map[i] = tmp;
    }
    for q in queries.iter() {
        let mut diff = map[q[0] as usize] ^ map[(q[1] + 1) as usize];
        let mut cnt = 0;
        while diff > 0 {
            diff &= diff - 1;
            cnt += 1;
        }
        ans.push(cnt / 2 <= q[2]);
    }
    ans
}

#[test]
fn test_1177() {
    assert_eq!(
        can_make_pali_queries("abcda".to_owned(), vec![vec![3, 3, 0], vec![1, 2, 0]]),
        vec![true, false]
    );
}
