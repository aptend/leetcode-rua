pub fn gray_code(n: i32) -> Vec<i32> {
    let mut ans = vec![0];
    for i in 0..n {
        let base = 2i32.pow(i as u32);
        let k = ans.len();
        for j in (0..k).rev() {
            ans.push(base + ans[j]);
        }
    }
    ans
}

#[test]
fn test_89() {
    assert_eq!(vec![0, 1], gray_code(1));
    assert_eq!(
        vec![
            0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28,
            20, 21, 23, 22, 18, 19, 17, 16
        ],
        gray_code(5)
    );
}
