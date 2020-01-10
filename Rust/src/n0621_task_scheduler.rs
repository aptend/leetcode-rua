pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
    if tasks.is_empty() {
        return 0;
    }
    let mut task_cnt = vec![0; 26];
    for ch in tasks.into_iter() {
        let idx = (ch as u8 - b'A') as usize;
        task_cnt[idx] += 1;
    }
    task_cnt.sort_unstable();
    let mut ans = 0;
    while task_cnt[25] != 0 {
        for i in 0..=n as usize {
            if task_cnt[25] <= 0 {
                break;
            }
            if i < 26 && task_cnt[25 - i] > 0 {
                task_cnt[25 - i] -= 1;
            }
            ans += 1
        }
        task_cnt.sort_unstable();
    }
    ans
}

#[test]
fn test_621() {
    assert_eq!(8, least_interval(vec!['A', 'A', 'A', 'B', 'B', 'B'], 2));
    assert_eq!(
        16,
        least_interval(
            vec!['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
            2
        )
    );
}
