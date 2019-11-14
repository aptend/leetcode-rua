use std::cmp::Reverse;
pub fn reconstruct_queue(people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let mut p = people;
    p.sort_unstable_by_key(|x| (Reverse(x[0]), x[1]));
    let mut ans = vec![];
    for person in p.into_iter() {
        ans.insert(person[1] as usize, person);
    }
    ans
}

#[test]
fn test_406() {
    assert_eq!(
        vec![
            vec![5, 0],
            vec![7, 0],
            vec![5, 2],
            vec![6, 1],
            vec![4, 4],
            vec![7, 1]
        ],
        reconstruct_queue(vec![
            vec![7, 0],
            vec![4, 4],
            vec![7, 1],
            vec![5, 0],
            vec![6, 1],
            vec![5, 2]
        ])
    );
}
