pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
    let mut pos: std::collections::VecDeque<usize> = (0..deck.len()).collect();
    let mut ans = vec![0; deck.len()];
    let mut deck = deck;
    deck.sort_unstable();
    for &card in &deck {
        let first = pos.pop_front().unwrap();
        ans[first] = card;
        pos.rotate_left(std::cmp::min(1, pos.len()));
    }
    ans
}

#[test]
fn test_950() {
    assert_eq!(
        vec![2, 13, 3, 11, 5, 17, 7],
        deck_revealed_increasing(vec![17, 13, 11, 2, 3, 5, 7])
    );
    assert_eq!(
        vec![1, 9, 2, 7, 3, 11, 4, 8, 5, 10, 6],
        deck_revealed_increasing(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    );
}
