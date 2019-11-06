pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
    let flat: Vec<i32> = matrix.into_iter().flatten().collect();
    flat.binary_search(&target).is_ok()
}

#[test]
fn test_74() {
    let m = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 50]];
    assert_eq!(false, search_matrix(Vec::<Vec<i32>>::new(), 0));
    assert_eq!(false, search_matrix(m.clone(), 2));
    assert_eq!(true, search_matrix(m.clone(), 5));
    assert_eq!(true, search_matrix(m.clone(), 7));
    assert_eq!(false, search_matrix(m.clone(), 8));
    assert_eq!(false, search_matrix(m.clone(), 13));
}
